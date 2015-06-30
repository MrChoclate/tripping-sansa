# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_category_assignment_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='assigment',
            field=models.OneToOneField(to='api.Product_category_assignment', null=True, related_name='category', blank=True),
        ),
    ]
