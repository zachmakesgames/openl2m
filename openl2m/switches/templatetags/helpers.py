from django.conf import settings
from django import template
from django.template import Template, Context
from django.utils.html import mark_safe

from switches.models import *
from switches.constants import *
from switches.utils import bytes_to_hex_string_ethernet, bytes_ethernet_to_oui
from switches.connect.constants import *
from switches.connect.oui.oui import get_vendor_from_oui

# see https://docs.djangoproject.com/en/2.2/ref/templates/api/
# and https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/

register = template.Library()


@register.filter
def bitwise_and(value, arg):
    """
    This is used in some templates to show the bitmat values of switch.capabilities
    """
    return bool(value & arg)


def build_url_string(values):
    """
    Build a external url string from the url values dict() given
    """
    if 'target' in values.keys():
        s = "<a target=\"%s\" " % values['target']
    else:
        s = "<a "
    s += "href=\"%s\"" % values['url']
    if 'hint' in values.keys():
        s += " title=\"%s\"" % values['hint']
    s += ">"
    if 'fa_icon' in values.keys():
        s += "<i fa %s aria-hidden=\"true\"></i>" % values['fa_icon']
    elif 'icon' in values.keys():
        s += ("<img src=\"%s\" alt=\"%s\" height=\"24\" width=\"24\">" % (values['icon'], values['alt']))
    s += "</a>"
    return s


def get_switch_link(group, switch):
    s = ''
    if switch.status == SWITCH_STATUS_ACTIVE and switch.snmp_profile:
        s = "<li class=\"list-group-item\">"
        if False and switch.description:
            s = "%s<span title=\"%s\">" % (s, switch.description)
        # do proper indenting:
        indent = ''
        for i in range(switch.indent_level):
            indent = "&nbsp;&nbsp;&nbsp;%s" % indent
        if switch.default_view == SWITCH_VIEW_BASIC:
            s = "%s%s<a href=\"/switches/%d/%d/\">" % (s, indent, group.id, switch.id)
        else:
            s = "%s<a href=\"/switches/%d/%d/details/\">" % (s, group.id, switch.id)
        s = "%s%s</a>" % (s, switch.name)
        if False and switch.description:
            s = "%s</span>" % s
        s = "%s</li>" % s
    return s


@register.filter
def get_my_switchgroups(groups):
    """
    Get all the switchgroups and their switches
    """
    c = len(groups)
    if not c:
        s = '<strong>You are not a member of any switch groups!</strong></br>Please contact the application administrator!'
        return mark_safe(s)
    # at least one group:
    if c == 1:
        # one group only
        s = "<h4>My Switch Group</h4>"
    else:
        s = "<h4>My Switch Groups</h4>"

    # start groups wrapper:
    s = "%s\n\n <div>\n" % s    # end panel-heading

    # now list the groups:
    for (group_name, group) in groups.items():
        # header for collapsible items, i.e. the switchgroup name
        s = "%s\n <div class=\"panel-group\">\n   <div class=\"panel panel-default\">\n   <div class=\"panel-heading\">" % s
        if False and group.description:
            s = "%s\n  <span title=\"%s\">" % group.description
        s = "%s<a data-toggle=\"collapse\" href=\"#group%d\">" % (s, group.id)
        if group.display_name:
            s = "%s%s" % (s, group.display_name)
        else:
            s = "%s%s" % (s, group.name)
        s = "%s</a>" % s
        if group.read_only:
            s = "%s (r/o)" % s
        if False and group.description:
            s = "%s</span>" % s
        s = "%s</div>" % s  # this /div ends panel-heading

        # the collapsible items:
        s = "%s\n   <div id=\"group%d\" class=\"panel-collapse" % (s, group.id)
        # if only 1 group, show all items
        if c > 1:
            s = "%s collapse" % s
        s = "%s\">\n    <ul class=\"list-group\">" % s
        for member in SwitchGroupMembership.objects.filter(switchgroup=group):
            s = "%s\n     %s" % (s, get_switch_link(group, member.switch))
        s = "%s\n    </ul>\n   </div>" % s  # /div ends panel-collapse

        # and end this group header and group:
        s = "%s\n  </div>\n  </div>\n" % s     # end panel-default and panel-group

    # end groups wrapper, and 'panel panel-default'
    s = "%s\n </div>\n" % s
    return mark_safe(s)


@register.filter
def get_switch_info_url_links(switch):
    """
    Get the info url(s) for the switch expanded from the settings file variable
    """
    links = ''
    if settings.SWITCH_INFO_URLS:
        for u in settings.SWITCH_INFO_URLS:
            # the switch.nms_id field is optional. If used in URL, check that it is set!
            if 'url' in u.keys():
                if u['url'].find('switch.nms_id') > -1:
                    # found it, but is the value set:
                    if not switch.nms_id:
                        # nms_id not set, skipping this switch
                        continue
            template = Template(build_url_string(u))
            context = Context({'switch': switch})
            links += template.render(context)
    return mark_safe(links)


@register.filter
def get_interface_info_links(switch, iface):
    """
    Get the info url(s) for the interface expanded from the settings file variable
    """
    links = ''
    if settings.INTERFACE_INFO_URLS:
        for u in settings.INTERFACE_INFO_URLS:
            template = Template(build_url_string(u))
            context = Context({
                'switch': switch,
                'iface': iface})
            links += template.render(context)
    return mark_safe(links)


@register.filter
def get_vlan_info_links(vlan):
    """
    Get the info url(s) for the Vlan() expanded from the settings file variable
    """
    links = ''
    if settings.VLAN_INFO_URLS:
        # do this for all URLs listed:
        for u in settings.VLAN_INFO_URLS:
            template = Template(build_url_string(u))
            context = Context({'vlan': vlan, })
            links += template.render(context)
    return mark_safe(links)


@register.filter
def get_ethernet_info_links(ethernet):
    """
    Get the info url(s) for the EthernetAddress() expanded from the settings file variable
    """
    links = ''
    if settings.ETHERNET_INFO_URLS:
        # do this for all URLs listed:
        for u in settings.ETHERNET_INFO_URLS:
            template = Template(build_url_string(u))
            context = Context({'ethernet': ethernet, })
            links += template.render(context)
    return mark_safe(links)


@register.filter
def get_ip4_info_links(ip4_address):
    """
    Get the info url(s) for the ipv4 address (string format) expanded from the settings file variable
    """
    links = ''
    if settings.IP4_INFO_URLS:
        # do this for all URLs listed:
        for u in settings.IP4_INFO_URLS:
            template = Template(build_url_string(u))
            context = Context({'ip4': ip4_address, })
            links += template.render(context)
    return mark_safe(links)


@register.filter
def get_ip6_info_links(ip4_address):
    """
    Get the info url(s) for the ipv6 address (string format) expanded from the settings file variable
    """
    links = ''
    if settings.IP6_INFO_URLS:
        # do this for all URLs listed:
        for u in settings.IP6_INFO_URLS:
            template = Template(build_url_string(u))
            context = Context({'ip6': ip6_address, })
            links += template.render(context)
    return mark_safe(links)


@register.filter
def get_interface_link(switch, iface):
    """
    Return the HTML data for this interface, including status/type images, etc.
    """
    # start with up/down color for interface
    if iface.ifAdminStatus == IF_ADMIN_STATUS_UP:
        info = " bgcolor=\"%s\" " % settings.BGCOLOR_IF_ADMIN_UP
    else:
        info = " bgcolor=\"%s\" " % settings.BGCOLOR_IF_ADMIN_DOWN
    # next add the NMS link for this interface
    info += get_interface_info_links(switch, iface)
    # next make linkable if we can manage it
    if iface.manageable:
        if iface.ifAdminStatus == IF_ADMIN_STATUS_UP:
            info += ("<a onclick=\"return confirm_change('Are you sure you want to DISABLE %s ?')\" \
                     href=\"/switches/%d/%d/%d/admin/%d/\" title=\"Click here to Disable %s\">%s</a>" %
                     (iface.name, group.id, switch.id, iface.ifIndex, IF_ADMIN_STATUS_DOWN, iface.name))
        else:
            info += ("<a onclick=\"return confirm_change('Are you sure you want to ENABLE %s ?')\" \
                     href=\"/switches/%d/%d/%d/admin/%d/\" title=\"Click here to Enable %s\">%s</a>" %
                     (iface.name, group.id, switch.id, iface.ifIndex, IF_ADMIN_STATUS_UP, iface.name))
    else:
        info += " %s " % iface.name

    # start with up/down color for interface
    if iface.ifAdminStatus == IF_ADMIN_STATUS_UP:
        info += "&nbsp;&nbsp;<img src=\"/static/img/enabled-24.png\" \
                 alt=\"Interface Enabled\" title=\"Interface is Enabled\">"
    else:
        info += "&nbsp;&nbsp;<img src=\"/static/img/disabled-24.png\" \
                 alt=\"Interface Disabled\" title=\"Interface is Disabled\">"

    # finally, add icons representing interface 'features'
    if iface.is_tagged:
        info += "&nbsp;&nbsp;<img src=\"/static/img/trunk-24.png\" \
                 alt=\"Tagged/Trunked Interface\" title=\"Tagged/Trunked Interface\">"
    if iface.voice_vlan:
        info += "&nbsp;&nbsp;<img src=\"/static/img/voicevlan-24.png\" \
                 alt=\"Voice VLAN\" title=\"Voice VLAN %d>\"" % iface.voice_vlan

    return mark_safe(info)


@register.filter
def get_device_class(device):
    """
    Return an html string that represent the data of the device given.
    A device is a switch, a stack, or a switch in that stack.
    """
    return ENTITY_CLASS_NAME[device.type]


@register.filter
def get_lldp_info(neighbor):
    """
    Return an hmtl img string that represents the lldp neighbor device and capabilities
    To keep things simple, we return a single icon, even when multiple capabilities exist.
    """

    info = ''
    # add an image for the capabilities
    img_format = "<img src=\"/static/img/%s\" title=\"%s\" height=\"24\" width=\"24\">&nbsp;"
    capabilities = int(neighbor.capabilities[0])
    if capabilities & LLDP_CAPA_BITS_WLAN:
        info += img_format % ('device-wifi-24.png', 'Wireless AP')
    elif capabilities & LLDP_CAPA_BITS_PHONE:
        info += img_format % ('device-phone-24.png', 'VOIP Phone')
    elif capabilities & LLDP_CAPA_BITS_ROUTER:
        info += img_format % ('device-router-24.png', 'Router or Switch')
    elif capabilities & LLDP_CAPA_BITS_STATION:
        info += img_format % ('device-station-24.png', 'Workstation or Server')
    elif capabilities & LLDP_CAPA_BITS_BRIDGE:
        info += img_format % ('device-switch-24.png', 'Switch')
    elif capabilities & LLDP_CAPA_BITS_REPEATER:
        info += img_format % ('device-switch-24.png', 'Hub or Repeater')
    # elif capabilities & LLDP_CAPA_BITS_DOCSIS:
    # unlikely to see this!
    #    icon = "unknown"
    elif capabilities & LLDP_CAPA_BITS_OTHER:
        info += img_format % ('device-unknown-24.png', 'Other Capabilities')
    else:
        info += img_format % ('device-unknown-24.png', 'Capabilities NOT Advertized ')

    name = ''
    if neighbor.sys_name:
        name = neighbor.sys_name
    else:
        name = 'Unknown'

    chassis_info = ''
    if neighbor.chassis_string and neighbor.chassis_type:
        # use the chassis info, if found.
        if neighbor.chassis_type == LLDP_CHASSIC_TYPE_ETH_ADDR:
            eth = bytes_to_hex_string_ethernet(neighbor.chassis_string)
            # vendor = get_vendor_from_oui(bytes_ethernet_to_oui(neighbor.chassis_string))
            # name = "%s (%s)" % (eth, vendor)
            chassis_info = eth
        elif neighbor.chassis_type == LLDP_CHASSIC_TYPE_NET_ADDR:
            net_addr_type = int(ord(neighbor.chassis_string[0]))
            if net_addr_type == IANA_TYPE_IPV4:
                bytes = neighbor.chassis_string[1:]
                separator = '.'
                format = "%d"
                chassis_info = 'IPv4 Address'
                chassis_info = separator.join(format % ord(b) for b in bytes)
            elif net_addr_type == IANA_TYPE_IPV6:
                chassis_info = 'IPv6 Address'
            else:
                chassis_info = 'Unknown Address Type'

    if neighbor.sys_descr:
        info += "<abbr title=\"%s\">%s - %s</abbr>" % (neighbor.sys_descr, name, chassis_info)
    else:
        info += "%s - %s" % (name, chassis_info)

    return mark_safe(info)


@register.filter
def get_poe_pse_status(status):
    """
    Return the string representing the PSE STATUS
    """
    if status == POE_PSE_STATUS_ON:
        return 'Enabled'
    if status == POE_PSE_STATUS_OFF:
        return 'Disabled'
    if status == POE_PSE_STATUS_FAULT:
        return 'Faulty'
    return 'Unknown'