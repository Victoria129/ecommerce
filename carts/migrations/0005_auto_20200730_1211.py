# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-07-30 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20200730_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='update',
            new_name='updated',
        ),
    ]
