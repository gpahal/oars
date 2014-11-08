# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(related_name='prerequisites_rel_+', to='oars.Course', blank=True),
        ),
    ]
