# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0007_auto_20141126_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teaching_assistants',
            field=models.ManyToManyField(to='oars.Student', blank=True, null=True),
            preserve_default=True,
        ),
    ]
