# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0003_auto_20141106_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(related_name='prerequisites_rel_+', to=b'oars.Course', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to=b'oars.Professor', blank=True),
        ),
    ]
