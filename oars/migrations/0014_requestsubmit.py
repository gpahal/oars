# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0013_request_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('status', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Not submitted'), (1, 'Submitted'), (2, 'Submit & accepted'), (4, 'Submit & rejected')])),
                ('student', models.ForeignKey(to='oars.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
