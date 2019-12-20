# Generated by Django 2.2.6 on 2019-10-14 17:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name as shown to the user', max_length=32)),
                ('os', models.CharField(help_text='The switch OS name, for easier displaying & sorting', max_length=32)),
                ('description', models.CharField(blank=True, help_text='Explanation of command, shown as hover-over to user', max_length=100)),
                ('type', models.PositiveSmallIntegerField(choices=[[0, 'Global'], [1, 'Interface']], default=1, help_text='Type of command, i.e. for the switch (global), or on chosen interface', verbose_name='Command type')),
                ('command', models.CharField(help_text='The command. Use %s for interface name', max_length=64, verbose_name='Command')),
            ],
            options={
                'verbose_name': 'Command',
                'verbose_name_plural': 'Commands',
                'ordering': ['type', 'name', 'os'],
                'unique_together': {('name', 'type', 'os')},
            },
        ),
        migrations.CreateModel(
            name='CommandList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('global_commands', models.ManyToManyField(blank=True, help_text='List of global "show" commands user can send to switch.', limit_choices_to={'type': 0}, related_name='global_commands', to='switches.Command', verbose_name='Global commands to send to switch.')),
                ('global_commands_staff', models.ManyToManyField(blank=True, help_text='List of global "show" commands Staff users can send to switch.', limit_choices_to={'type': 0}, related_name='global_commands_staff', to='switches.Command', verbose_name='Global commands for Staff.')),
                ('interface_commands', models.ManyToManyField(blank=True, help_text='List of contextual "show interface" commands user can send to switch. %s will be replaced with interface name.', limit_choices_to={'type': 1}, related_name='interface_commands', to='switches.Command', verbose_name='Interface commands to send to switch.')),
                ('interface_commands_staff', models.ManyToManyField(blank=True, help_text='List of contextual "show interface" commands Staff users can send to switch. %s will be replaced with interface name.', limit_choices_to={'type': 1}, related_name='interface_commands_staff', to='switches.Command', verbose_name='Interface commands for Staff.')),
            ],
            options={
                'verbose_name': 'Commands List',
                'verbose_name_plural': 'Commands Lists',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NetmikoProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(default='username', max_length=32, verbose_name='Username')),
                ('password', models.CharField(default='password', max_length=64, verbose_name='Password')),
                ('device_type', models.CharField(choices=[('a10', 'a10'), ('accedian', 'accedian'), ('alcatel_aos', 'alcatel_aos'), ('alcatel_sros', 'alcatel_sros'), ('apresia_aeos', 'apresia_aeos'), ('arista_eos', 'arista_eos'), ('aruba_os', 'aruba_os'), ('avaya_ers', 'avaya_ers'), ('avaya_vsp', 'avaya_vsp'), ('brocade_fastiron', 'brocade_fastiron'), ('brocade_netiron', 'brocade_netiron'), ('brocade_nos', 'brocade_nos'), ('brocade_vdx', 'brocade_vdx'), ('brocade_vyos', 'brocade_vyos'), ('calix_b6', 'calix_b6'), ('checkpoint_gaia', 'checkpoint_gaia'), ('ciena_saos', 'ciena_saos'), ('cisco_asa', 'cisco_asa'), ('cisco_ios', 'cisco_ios'), ('cisco_nxos', 'cisco_nxos'), ('cisco_s300', 'cisco_s300'), ('cisco_tp', 'cisco_tp'), ('cisco_wlc', 'cisco_wlc'), ('cisco_xe', 'cisco_xe'), ('cisco_xr', 'cisco_xr'), ('cloudgenix_ion', 'cloudgenix_ion'), ('coriant', 'coriant'), ('dell_dnos9', 'dell_dnos9'), ('dell_force10', 'dell_force10'), ('dell_isilon', 'dell_isilon'), ('dell_os10', 'dell_os10'), ('dell_os6', 'dell_os6'), ('dell_os9', 'dell_os9'), ('dell_powerconnect', 'dell_powerconnect'), ('eltex', 'eltex'), ('endace', 'endace'), ('enterasys', 'enterasys'), ('extreme', 'extreme'), ('extreme_ers', 'extreme_ers'), ('extreme_exos', 'extreme_exos'), ('extreme_netiron', 'extreme_netiron'), ('extreme_nos', 'extreme_nos'), ('extreme_slx', 'extreme_slx'), ('extreme_vdx', 'extreme_vdx'), ('extreme_vsp', 'extreme_vsp'), ('extreme_wing', 'extreme_wing'), ('f5_linux', 'f5_linux'), ('f5_ltm', 'f5_ltm'), ('f5_tmsh', 'f5_tmsh'), ('flexvnf', 'flexvnf'), ('fortinet', 'fortinet'), ('generic_termserver', 'generic_termserver'), ('hp_comware', 'hp_comware'), ('hp_procurve', 'hp_procurve'), ('huawei', 'huawei'), ('huawei_vrpv8', 'huawei_vrpv8'), ('ipinfusion_ocnos', 'ipinfusion_ocnos'), ('juniper', 'juniper'), ('juniper_junos', 'juniper_junos'), ('linux', 'linux'), ('mellanox', 'mellanox'), ('mikrotik_routeros', 'mikrotik_routeros'), ('mikrotik_switchos', 'mikrotik_switchos'), ('mrv_lx', 'mrv_lx'), ('mrv_optiswitch', 'mrv_optiswitch'), ('netapp_cdot', 'netapp_cdot'), ('netscaler', 'netscaler'), ('oneaccess_oneos', 'oneaccess_oneos'), ('ovs_linux', 'ovs_linux'), ('paloalto_panos', 'paloalto_panos'), ('pluribus', 'pluribus'), ('quanta_mesh', 'quanta_mesh'), ('rad_etx', 'rad_etx'), ('ruckus_fastiron', 'ruckus_fastiron'), ('ubiquiti_edge', 'ubiquiti_edge'), ('ubiquiti_edgeswitch', 'ubiquiti_edgeswitch'), ('vyatta_vyos', 'vyatta_vyos'), ('vyos', 'vyos')], default='hp_comware', max_length=64, verbose_name='Netmiko device_type field')),
                ('enable_password', models.CharField(blank=True, max_length=64, null=True, verbose_name='Netmiko enable password, e.g. for Cisco devices (optional)')),
                ('tcp_port', models.PositiveIntegerField(default=22, verbose_name='Tcp port')),
                ('verify_hostkey', models.BooleanField(default=False, verbose_name='Verify the ssl host key')),
            ],
            options={
                'verbose_name': 'Netmiko Profile',
                'verbose_name_plural': 'Netmiko Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SnmpProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('version', models.PositiveSmallIntegerField(choices=[(2, '2c'), (3, '3')], default=3)),
                ('community', models.CharField(blank=True, max_length=64, null=True, verbose_name='v1/v2c Community name')),
                ('username', models.CharField(blank=True, max_length=32, null=True, verbose_name='v3 Username')),
                ('passphrase', models.CharField(blank=True, max_length=64, null=True, verbose_name='v3 Authentication passphrase')),
                ('priv_passphrase', models.CharField(blank=True, max_length=64, null=True, verbose_name='v3 Privacy passphrase')),
                ('auth_protocol', models.PositiveSmallIntegerField(choices=[(0, 'none'), (1, 'MD5'), (2, 'SHA')], default=2)),
                ('priv_protocol', models.PositiveSmallIntegerField(choices=[(0, 'none'), (1, 'DES'), (3, 'AES')], default=3)),
                ('sec_level', models.PositiveSmallIntegerField(choices=[(0, 'NoAuth-NoPriv'), (1, 'Auth-NoPriv'), (2, 'Auth-Priv')], default=2, verbose_name='Security level')),
                ('context_name', models.CharField(blank=True, help_text='SNMP v3 contextName field. Mostly left blank. Only set if you know what this is! (not used yet)', max_length=256, null=True, verbose_name='v3 Context Name')),
                ('context_engine_id', models.CharField(blank=True, help_text='SNMP v3 contextEngineID field. Mostly left blank. Only set if you know what this is! (not used yet)', max_length=256, null=True, verbose_name='v3 Context EngineID')),
                ('udp_port', models.PositiveIntegerField(default=161, verbose_name='SNMP Udp port')),
            ],
            options={
                'verbose_name': 'SNMP Profile',
                'verbose_name_plural': 'SNMP Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('indent_level', models.SmallIntegerField(default=0, help_text='Tab indentation level, helps organize the switchgroup view', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Indentation level')),
                ('read_only', models.BooleanField(default=False, verbose_name='Read-Only access')),
                ('default_view', models.PositiveSmallIntegerField(choices=[[0, 'Basic'], [1, 'Details']], default=0, help_text='Default view. Details shows Ethernet, ARP, LLDP immediately.', verbose_name='Default View')),
                ('allow_poe_toggle', models.BooleanField(default=False, verbose_name='If set, allow PoE toggle on all interfaces')),
                ('status', models.PositiveSmallIntegerField(choices=[[1, 'Active'], [0, 'Offline'], [2, 'Planned'], [3, 'Staged'], [4, 'Failed'], [5, 'Inventory'], [6, 'Decommissioning']], default=1, verbose_name='Status')),
                ('primary_ip4', models.CharField(blank=True, help_text='IP address or hostname', max_length=64, null=True, unique=True, verbose_name='Management IPv4')),
                ('comments', models.TextField(blank=True)),
                ('snmp_hostname', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='SNMP Hostname')),
                ('snmp_bulk_read_count', models.PositiveIntegerField(default=0, verbose_name='SNMP Bulk Reads')),
                ('snmp_read_count', models.PositiveIntegerField(default=0, verbose_name='SNMP Reads')),
                ('snmp_write_count', models.PositiveIntegerField(default=0, verbose_name='SNMP Writes')),
                ('snmp_oid', models.CharField(blank=True, default='', max_length=100, verbose_name='SNMP systemOID for this switch')),
                ('snmp_capabilities', models.BigIntegerField(default=0, help_text='Bitmap of switch snmp capabilities', verbose_name='Bitmap of switch snmp capabilities')),
                ('command_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='command_list', to='switches.CommandList')),
                ('netmiko_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='netmiko_profile', to='switches.NetmikoProfile')),
                ('snmp_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='snmp_profile', to='switches.SnmpProfile')),
            ],
            options={
                'verbose_name_plural': 'Switches',
                'ordering': ['name'],
                'unique_together': {('primary_ip4', 'snmp_profile')},
            },
        ),
        migrations.CreateModel(
            name='SwitchGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('display_name', models.CharField(blank=True, help_text="Display name allows you to override the group name. This is mostly useful for auto-created LDAP groups, that may not have 'display friendly' names", max_length=64, verbose_name='Display name overrides the group name')),
                ('description', models.CharField(blank=True, help_text='Description is shown when hovering over SwitchGroup in main menu.', max_length=120)),
                ('read_only', models.BooleanField(default=False, help_text='If set, this group becomes read-only for all users, except Admins', verbose_name='Read-Only access')),
                ('allow_poe_toggle', models.BooleanField(default=False, help_text='If set, allow PoE toggle on all interfaces', verbose_name='Poe Toggle All')),
                ('edit_if_descr', models.BooleanField(default=False, help_text='If set, allow interface descriptions to be edited', verbose_name='Edit Port Description')),
                ('comments', models.TextField(blank=True, help_text='Comment are for additional admin observations only, e.g. ticket #, notes about usage. etc.Comments are not shown in the user interface.')),
            ],
            options={
                'verbose_name': 'Switch Group',
                'verbose_name_plural': 'Switch Groups',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VLAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('vid', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4094)], verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'VLAN',
                'verbose_name_plural': 'VLANs',
                'ordering': ['vid', 'name'],
                'unique_together': {('vid', 'name')},
            },
        ),
        migrations.CreateModel(
            name='VlanGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('vlans', models.ManyToManyField(blank=True, help_text='A grouping of VLANs, e.g. by department', related_name='vlangroups', to='switches.VLAN', verbose_name='VLANs in group')),
            ],
            options={
                'verbose_name': 'VLAN Group',
                'verbose_name_plural': 'VLAN Groups',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SwitchGroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='switches.Switch')),
                ('switchgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='switches.SwitchGroup')),
            ],
            options={
                'ordering': ('switchgroup', 'order'),
            },
        ),
        migrations.AddField(
            model_name='switchgroup',
            name='switches',
            field=models.ManyToManyField(blank=True, help_text='For all the switches in this group, group users can manage any interface with a PVID in this list of VLANs. Other interfaces can not be managed.', related_name='switchgroups', through='switches.SwitchGroupMembership', to='switches.Switch', verbose_name='Member Switches'),
        ),
        migrations.AddField(
            model_name='switchgroup',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='Users add to this group have access to the switches in this group, and the ports on the vlans in this group.', related_name='switchgroups', to=settings.AUTH_USER_MODEL, verbose_name='Group Users'),
        ),
        migrations.AddField(
            model_name='switchgroup',
            name='vlan_groups',
            field=models.ManyToManyField(blank=True, help_text='For all the switches in this group, users in this group can manage any interface with a PVID in these VLAN Groups. Interfaces on VLANs not listed in these groups or the individual vlans below cannot be managed.', related_name='vlangroups', to='switches.VlanGroup', verbose_name='Allowed VLAN Groups'),
        ),
        migrations.AddField(
            model_name='switchgroup',
            name='vlans',
            field=models.ManyToManyField(blank=True, help_text='For all the switches in this group, users in this group can manage any interface with a PVID on these VLANs. Interfaces on VLANs not listed here or in the Vlan Groups above cannot be managed.', related_name='vlans', to='switches.VLAN', verbose_name='Allowed VLANs'),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('if_index', models.PositiveSmallIntegerField(default=0, verbose_name='SNMP interface index')),
                ('ip_address', models.TextField(default='0.0.0.0', help_text='The user IP address that created the log entry', max_length=20)),
                ('type', models.PositiveSmallIntegerField(choices=[[0, 'View'], [1, 'Change'], [2, 'Warning'], [3, 'Error'], [4, 'Command']], default=0, verbose_name='Type of Log Entry')),
                ('action', models.PositiveSmallIntegerField(choices=[[0, 'View Switch Groups'], [1, 'View Switch'], [2, 'View Interface'], [3, 'View PoE'], [4, 'View Vlans'], [5, 'View LLDP'], [6, 'Viewing All Logs'], [7, 'Viewing Site Statistics'], [100, 'Reloading Switch Data'], [101, 'New System ObjectID Found'], [102, 'New System Name Found'], [90, 'Login'], [91, 'Logout'], [92, 'Inactivity Logout'], [103, 'Interface Disable'], [104, 'Interface Enable'], [105, 'Interface Toggle'], [106, 'Interface PoE Disable'], [107, 'Interface PoE Enable'], [108, 'Interface PoE Toggle'], [109, 'Interface PVID Vlan Change'], [110, 'Interface Description Change'], [111, 'Saving Configuration'], [112, 'Execute Command'], [113, 'Port PoE Fault'], [256, 'Undefined Vlan'], [257, 'Vlan Name Mismatch'], [258, 'SNMP Error']], default=1, verbose_name='Activity or Action to log')),
                ('description', models.TextField(blank=True, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='switches.SwitchGroup')),
                ('switch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='switches.Switch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Activity Logs',
                'ordering': ['timestamp'],
            },
        ),
    ]