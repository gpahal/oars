# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oars', '0003_course_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='oars.Course')),
                ('student', models.ForeignKey(to='oars.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='courseplan',
            unique_together=set([('course', 'student')]),
        ),
    ]
