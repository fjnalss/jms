# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perm',
            name='user',
            field=models.ManyToManyField(to='users.User', verbose_name='用户'),
        ),
    ]
