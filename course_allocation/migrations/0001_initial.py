# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Waiting'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('course', models.OneToOneField(to='oars_auth.Course')),
                ('student', models.OneToOneField(to='oars_auth.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
