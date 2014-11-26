# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0006_auto_20141121_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_current_course',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='teaching_assistants',
            field=models.ManyToManyField(to='oars.Student'),
            preserve_default=True,
        ),
    ]
