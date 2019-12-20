# Generated by Django 2.2.7 on 2019-11-26 18:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0004_auto_20191120_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='bulk_edit',
            field=models.BooleanField(default=True, help_text='If Bulk Edit is set, we allow multiple interfaces on this switch to be edited at once.', verbose_name='Bulk-editing of interfaces'),
        ),
        migrations.AddField(
            model_name='switchgroup',
            name='bulk_edit',
            field=models.BooleanField(default=True, help_text='If Bulk Edit is set, we can edit multiple interfaces at once on the switches in this group.', verbose_name='Bulk-editing of interfaces'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='command_list',
            field=models.ForeignKey(blank=True, help_text='This is the list of commands (if any) that can be executed on the switch.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='command_list', to='switches.CommandList'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='comments',
            field=models.TextField(blank=True, help_text='Add any additional information about this switch.'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='indent_level',
            field=models.SmallIntegerField(default=0, help_text='Tab indentation level, helps organize the switchgroup view.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Indentation level'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='netmiko_profile',
            field=models.ForeignKey(blank=True, help_text='The Netmiko Profile has all the settings to access the switch via SSH for additional command access.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='netmiko_profile', to='switches.NetmikoProfile'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='read_only',
            field=models.BooleanField(default=False, help_text='The checked, this switch will be read-only.', verbose_name='Read-Only access'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_bulk_read_count',
            field=models.PositiveIntegerField(default=0, help_text='SNMP Bulks read count performed on the switch.', verbose_name='SNMP Bulk Reads'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_capabilities',
            field=models.BigIntegerField(default=0, help_text='Bitmap of switch snmp capabilities.', verbose_name='Bitmap of switch snmp capabilities'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_hostname',
            field=models.CharField(blank=True, default='', help_text='The switch hostname as reported via snmp.', max_length=64, null=True, verbose_name='SNMP Hostname'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_oid',
            field=models.CharField(blank=True, default='', help_text='The switch OID as reported via snmp.', max_length=100, verbose_name='SNMP systemOID for this switch'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_profile',
            field=models.ForeignKey(blank=True, help_text='The SNMP Profile has all the settings to read/write data on the switch.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='snmp_profile', to='switches.SnmpProfile'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_read_count',
            field=models.PositiveIntegerField(default=0, help_text='SNMP read count performed on the switch.', verbose_name='SNMP Reads'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='snmp_write_count',
            field=models.PositiveIntegerField(default=0, help_text='SNMP write count performed on the switch.', verbose_name='SNMP Writes'),
        ),
        migrations.AlterField(
            model_name='switchgroup',
            name='read_only',
            field=models.BooleanField(default=False, help_text='If set, the switches in this group are read-only for all users, except Admins', verbose_name='Read-Only access'),
        ),
    ]