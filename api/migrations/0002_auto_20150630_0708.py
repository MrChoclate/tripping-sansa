# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('relation_type', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('related_product', models.ForeignKey(null=True, to='api.Product', blank=True, related_name='+')),
                ('relating_product', models.ForeignKey(null=True, to='api.Product', blank=True, related_name='+')),
            ],
        ),
        migrations.AddField(
            model_name='product_version',
            name='relationship',
            field=models.ForeignKey(null=True, to='api.Product_version_relationship', blank=True),
        ),
        migrations.AddField(
            model_name='product_version_relationship',
            name='related_version',
            field=models.ForeignKey(null=True, to='api.Product_version', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='product_version_relationship',
            name='relating_version',
            field=models.ForeignKey(null=True, to='api.Product_version', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_relationship',
            field=models.OneToOneField(null=True, to='api.Product_relationship', related_name='+', blank=True),
        ),
    ]
