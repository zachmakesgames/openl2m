#########################
#                       #
#   Required settings   #
#                       #
#########################

# This is a list of valid fully-qualified domain names (FQDNs) for the OpenL2M server. OpenL2M will not permit write
# access to the server via any other hostnames. The first FQDN in the list will be treated as the preferred name.
#
# Example: ALLOWED_HOSTS = ['openl2m.example.com', 'openl2m.internal.local']
ALLOWED_HOSTS = ['*']

# This key is used for secure generation of random numbers and strings. It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters in length and contain a mix of letters, numbers, and
# symbols. OpenL2M will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
# SECURITY WARNING: keep the secret key used in production secret!
# you can generate a key with the "openl2m/generate_secret_key.py" script.
SECRET_KEY = ''

# PostgreSQL database configuration.
DATABASE = {
    'NAME': 'openl2m',          # Database name
    'USER': 'openl2m',          # PostgreSQL username
    'PASSWORD': 'xxxxxxxxxxx',  # PostgreSQL password
    'HOST': 'localhost',        # Database server
    'PORT': '',                 # Database port (leave blank for default)
}

#########################
#                       #
#   Optional settings   #
#                       #
#########################

# Optionally display a persistent banner at the top and/or bottom of every page. HTML is allowed. To display the same
# content in both banners, define BANNER_TOP and set BANNER_BOTTOM = BANNER_TOP.
BANNER_TOP = 'Top Banner Information Line'
BANNER_BOTTOM = 'Bottom Banner Line'

# Text to include on the login page above the login form. HTML is allowed.
BANNER_LOGIN = 'Login Banner'

# Base URL path if accessing OpenL2M within a directory. For example, if installed at http://example.com/openl2m/, set:
# BASE_PATH = 'openl2m/'
BASE_PATH = ''

# Keep activity log entries for this many day. 0 disables (keep forever)
LOG_MAX_AGE = 180

# API Cross-Origin Resource Sharing (CORS) settings. If CORS_ORIGIN_ALLOW_ALL is set to True, all origins will be
# allowed. Otherwise, define a list of allowed origins using either CORS_ORIGIN_WHITELIST or
# CORS_ORIGIN_REGEX_WHITELIST. For more information, see https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    # 'hostname.example.com',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    # r'^(https?://)?(\w+\.)?example\.com$',
]

# The length of time (in seconds) for which a user will remain logged into the web UI before being prompted to
# re-authenticate. (Default: 1800 [30 minutes])
LOGIN_TIMEOUT = 1800

# Setting this to True will display a "maintenance mode" banner at the top of every page.
MAINTENANCE_MODE = False

# Determine how many objects to display per page within a list. (Default: 50)
PAGINATE_COUNT = 50

# When determining the primary IP address for a device, IPv6 is preferred over IPv4 by default. Set this to True to
# prefer IPv4 instead.
PREFER_IPV4 = True      # IPv6 has not been tested!

# By default, OpenL2M will store session data in the database. Alternatively, a file path can be specified here to use
# local file storage instead. (This can be useful for enabling authentication on a standby instance with read-only
# database access.) Note that the user as which OpenL2M runs must have read and write permissions to this path.
SESSION_FILE_PATH = None

# Time zone (default: UTC)
TIME_ZONE = 'UTC'

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = 'N j, Y'
SHORT_DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'g:i a'
SHORT_TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'N j, Y g:i a'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'

# Delay in seconds when we disable and re-enable an interface, or PoE
PORT_TOGGLE_DELAY = 5

# PoE toggling, disable PoE, wait this long, and enable property
POE_TOGGLE_DELAY = 5

# If enabled, allow PoE enable/disable for all users with access to switch,
# regardless of other access to the interface
ALWAYS_ALLOW_POE_TOGGLE = False

# Customizable URLs for Switch, Interface, Ethernet and IP addresses
# 'url' is mandatory. 'hint' and 'target' are optional
# You can also use 'icon' and 'alt', or 'fa_icon'
# fa_icon refers to the Font Awesome v4.7 icon collection, and you reference it by name
# see  https://fontawesome.com/v4.7.0/icons/
# fa_icon takes precedence over icon/alt entries.

# Switch Info Urls is a list dictionaries with one or more links to put in front of the switch name.
# you can use the following template strings:
# {{ switch.name }}
# {{ switch.primary_ip4 }}
# {{ switch.nms_id }}
# {{ switch.snmp_hostname }}
SWITCH_INFO_URLS = [
    # This example is for Akips, and provides a direct link to the switch page in Akips:
    {
        'url': 'https://akips.yoursite.com/dashboard?mode=device;device_list={{ switch.name }};',
        'hint': 'Click here to see AKIPS data for this switch',
        'target': '_blank',
        'icon': '/static/img/nms-24.png',
        # or use the icon from Akip:
        # 'icon': 'https://akips.yoursite/img/favicon-32.png',
        'alt': 'Akips NMS Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
    # this would be a link to a LibreNMS or Observium page.
    # Note you have to fill in the "nms_id" field for each switch for this to work!
    {
        'url': 'https://librenms.yoursite.com/device/device={{ switch.nms_id }}/',
        'hint': 'Click here to see LibreNMS data for this switch',
        'target': '_blank',
        'icon': '/static/img/nms-24.png',
        # or use the icon from LibreNMS:
        # 'icon': 'http://librenms.yoursite.com/images/favicon-16x16.png',
        # or
        # 'icon': 'http://librenms.yoursite.com/images/favicon-32x32.png',
        # 'icon': 'http://librenms.yoursite.com/images/favicon.ico',
        'alt': 'LibreNMS Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
]

# Interface Info Urls is a list of dictionaries with one or more links to put in front of interfaces.
# you can use all the {{ switch }} templates above, as well as
# {{ iface.name }}
# {{ iface.index }} - the SNMP interface index ifIndex
# {{ iface.alias }} - the SNMP interface ifAlias aka 'description', probably not useful.
#
INTERFACE_INFO_URLS = [
    {
        'name': 'Akips',
        'url': 'https://akips.yoursite.com/dashboard?mode=interface;time=last3h;controls=interface;device={{ switch.name }};child={{ iface.name }}',
        'hint': 'Click here to see AKIPS data for this interface',
        'target': '_akips',
        'icon': '/static/img/nms-24.png',
        'alt': 'NMS Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
]

# VLAN Info Urls is a list of dictionaries with one or more links to put in front of vlans.
# you can use the following templates:
# {{ vlan.name }}   - the name :-)
# {{ vlan.id }}     - the vlan id :-)
#
VLAN_INFO_URLS = [
    {
        'name': 'IPAM',
        'url': 'https://ipam.yoursite.com/something/search?vlan={{ vlan.id }}',
        'hint': 'Click here to see IPAM data about this VLAN',
        'target': '_ipam',
        'icon': '/static/img/ipam.png',
        'alt': 'NMS Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
]


# IPv4 Address Info Urls is a list of dictionaries that will be links shown on found IP addresses.
# The idea is that you may want to provide a link to your device registration site, as well as your logging (eg Splunk)
# you can use the following templates:
# {{ ip4 }} - the ip v4 address x.x.x.x
IP4_INFO_URLS = [
    {
        'name': 'IPAM',
        'url': 'https://ipam.yoursite.com/something/search?ipv4={{ ip4 }}',
        'hint': 'Click here to see IPAM data about this IPv4 address',
        'target': '_ipam',
        'icon': '/static/img/ipam.png',
        'alt': 'NMS Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
    # another example, a direct link to an ELK stack log parser for the ipv4 addresses
    # note this is completely fictitious!
    {
        'name': 'ELK Stack',
        'url': 'https://elkstack.yoursite.com/search?eipv4={{ ip4 }}',
        'hint': 'Click here to see ELK Stack log data about this IPv4 address',
        'target': '_elk',
        'icon': '/static/img/general-info-24.png',
        'alt': 'ELK Stack Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
]


# Ethernet Info Urls is a list of dictionaries that will be links shown on found ethernet addresses.
# The idea is that you may want to provide a link to your device registration site, as well as your logging (eg Splunk)
# you can use the following templates:
# {{ ethernet.display_name }} - the formatted string xx:xx:xx:xx:xx:xx or xx-xx-xx-xx-xx-xx
ETHERNET_INFO_URLS = [
    {
        'name': 'IPAM',
        'url': 'https://ipam.yoursite.com/something/search?ethernet={{ ethernet.address }}',
        'hint': 'Click here to see IPAM data about this ethernet address',
        'target': '_ipam',
        'icon': '/static/img/ipam.png',
        'alt': 'NMS Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
    # another example, a direct link to an ELK stack log parser for the ethernet addresses
    # note this is completely fictitious!
    {
        'name': 'ELK Stack',
        'url': 'https://elkstack.yoursite.com/search?ethernet={{ ethernet.address }}',
        'hint': 'Click here to see ELK Stack log data about this eithernet address',
        'target': '_elk',
        'icon': '/static/img/general-info-24.png',
        'alt': 'ELK Stack Icon',
        # or use a Font Awesome icon:
        # 'fa_icon': 'fa-delicious',
    },
]

# Ethernet display format, either ETH_FORMAT_COLON = 0, ETH_FORMAT_HYPHEN = 1 or ETH_FORMAT_CISCO = 2
ETH_FORMAT = 0
# format ethernet address lower case or upper
ETH_FORMAT_UPPERCASE = False

# various regular expression to remove interfaces from the user
# this uses the Python 're' module.
#

# this regex matches the interface name, GigabitEthernetx/x/x
IFACE_HIDE_REGEX_IFNAME = "^TenGig"

# this regex matches the interface 'ifAlias' aka. the interface description
IFACE_HIDE_REGEX_IFDESCR = "BLUE"

# hide interfaces with speeds above this value in Mbps.
# e.g. hide 10G and above, set to 9500. 0 disables this filter.
IFACE_HIDE_SPEED_ABOVE = 9500

# if the new description matches this reg ex, do not allow it
IFACE_ALIAS_NOT_ALLOW_REGEX = "^Po|NOT ALLOWED"

# if the existing description start with this match,
# keep that part of the description when a user edits it.
# E.g. the below regex for port-patch descriptions of forma "D.nnn" to be kept
# while allowing 'real' descriptions to be added after it
IFACE_ALIAS_KEEP_BEGINNING_REGEX = "D.\d+"


# Custom Menu items, consisting of MENU_INFO_URLS and MENU_ON_RIGHT.

# MENU_ON_RIGHT = True, indicates the custom menu will be on the right side of the top bar
MENU_ON_RIGHT = True
# Menu Info URLs is a dictionary of dictionaries to form a menu structure of links in the top bar
# the initial dict() is the menu header name, and the containing dict() are the url links under it
#
# You can also use the Font Awesome v4.7.0 icons, from https://fontawesome.com/v4.7.0/icons/
# To use add an entry 'fa_icon': 'font-awesome-icon-name'
# This will take the place of the 'icon' entry (i.e. it will not be used if fa-icon is defined!)
#
"""
MENU_INFO_URLS = {}
MENU_INFO_URLS['Menu 1'] = [
    {
        'name': 'Entry 1',
        'url': 'http://example.com',
        'target': '_external',
        'fa_icon': 'fa-car'
    },
    {
        'name': 'Entry 2',
        'url': 'https://ssl.example.com',
        'target': '_external',
        'icon': '/static/img/ipam.png',
        'alt': 'Cyder Icon',
    },
]
MENU_INFO_URLS['Menu 2'] = [
    {
        'name': 'Entry 3',
        'url': 'http://example.com/test.php=test',
        'target': '_external',
        'icon': '/static/img/ipam.png',
        'alt': 'Cyder Icon',
    },
    {
        'name': 'Entry 4',
        'url': 'https://ssl.example.com',
        'target': '_external',
        'fa_icon': 'fa-address-book'
    },
]
"""

# Some html colors to choose interface admin status.
# Colors used behind the interface name (ie background):
# A great place for colors: https://www.rapidtables.com/web/color/
# Admin-UP, No Link:
BGCOLOR_IF_ADMIN_UP = "#98FB98"  # darker/lighter green
# Admin-UP, Link:
BGCOLOR_IF_ADMIN_UP_UP = "#ADFF2F"  # brighter green
# Admin disabled
BGCOLOR_IF_ADMIN_DOWN = "#EB5B5B"  # red

# SNMP related settings, normally not needed to change.
SNMP_TIMEOUT = 5    # in seconds
SNMP_RETRIES = 3
# this is the maximum count of MIB entities returned in a single reply in response to the get-bulk calls we make.
# note that some devices cannot handle the default 25, and you may need to lower this e.g. 10
# see the references in the documentation for more information.
SNMP_MAX_REPETITIONS = 25