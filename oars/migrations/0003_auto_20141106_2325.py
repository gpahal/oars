# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0002_auto_20141106_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(related_name='prerequisites_rel_+', null=True, to=b'oars.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to=b'oars.Professor', null=True),
        ),
    ]
