# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0009_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='added',
        ),
    ]
