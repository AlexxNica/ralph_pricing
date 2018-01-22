# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-24 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ralph_scrooge', '0011_usagetype_allow_no_daily_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='usagetype',
            name='support_team',
            field=models.CharField(blank=True, default='', help_text='Information about support team.', max_length=255, verbose_name='Support team'),
        ),
        migrations.AlterField(
            model_name='usagetype',
            name='allow_no_daily_usage',
            field=models.BooleanField(default=False, help_text='Skip validation of this UsageType for existing DailyUsages before recalculating costs'),
        ),
    ]