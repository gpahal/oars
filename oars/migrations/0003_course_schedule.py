# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0002_auto_20141119_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='schedule',
            field=models.CommaSeparatedIntegerField(default=b'101082,102082,104082', max_length=70),
            preserve_default=True,
        ),
    ]
