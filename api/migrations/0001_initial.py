# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure_value',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_category_assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_category_hierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_property_assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_version',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('product', models.OneToOneField(blank=True, to='api.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_version_relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_view_definition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('additionnal_characterization', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('si_unit', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value_with_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='View_definition_context',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('application_domain', models.CharField(max_length=100)),
                ('life_cycle_stage', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='View_definition_relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('relation_type', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='any_number_value',
            fields=[
                ('measure_value_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='api.Measure_value', serialize=False)),
                ('any_number_value', models.IntegerField()),
            ],
            bases=('api.measure_value',),
        ),
        migrations.CreateModel(
            name='View_definition_usage',
            fields=[
                ('view_definition_relationship_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='api.View_definition_relationship', serialize=False)),
            ],
            bases=('api.view_definition_relationship',),
        ),
        migrations.CreateModel(
            name='Assembly_component_relationship',
            fields=[
                ('view_definition_usage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='api.View_definition_usage', serialize=False)),
                ('location_indicator', models.TextField(null=True, blank=True)),
            ],
            bases=('api.view_definition_usage',),
        ),
        migrations.CreateModel(
            name='Component_upper_level_identification',
            fields=[
                ('assembly_component_relationship_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='api.Assembly_component_relationship', serialize=False)),
            ],
            bases=('api.assembly_component_relationship',),
        ),
        migrations.CreateModel(
            name='Next_assembly_usage',
            fields=[
                ('assembly_component_relationship_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='api.Assembly_component_relationship', serialize=False)),
            ],
            bases=('api.assembly_component_relationship',),
        ),
        migrations.CreateModel(
            name='Promissory_usage',
            fields=[
                ('assembly_component_relationship_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='api.Assembly_component_relationship', serialize=False)),
            ],
            bases=('api.assembly_component_relationship',),
        ),
    ]
