# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0005_auto_20141120_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='limit_exceeded',
        ),
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.CommaSeparatedIntegerField(default='101162,102162,104162', max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Waiting'), (1, 'Accepted'), (2, 'Rejected'), (4, 'Waiting (limit exceeded)')], default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='email address', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
    ]
