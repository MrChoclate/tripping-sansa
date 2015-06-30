# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150630_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category_assignment',
            name='products',
            field=models.ManyToManyField(related_name='categories', to='api.Product'),
        ),
    ]
