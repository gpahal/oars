# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('oars', '0004_auto_20141119_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.CommaSeparatedIntegerField(default=b'101162,102162,104162', max_length=70),
        ),
    ]
