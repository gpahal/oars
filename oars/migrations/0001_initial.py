# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, verbose_name='username', unique=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address')),
                ('full_name', models.CharField(blank=True, max_length=50, verbose_name='first name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('is_admin', models.BooleanField(help_text='Designates whether the user can log into the admin site.', default=False, verbose_name='admin status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(help_text='Required. 5 characters or fewer. Digits and uppercase letters only. ', validators=[django.core.validators.RegexValidator('^[A-Z]{2,3}[\\d]{3}[A-Z]?$', 'Enter a valid course code.', 'invalid')], max_length=7)),
                ('name', models.CharField(help_text='Required. 50 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid course name.', 'invalid')], max_length=50)),
                ('schedule', models.CommaSeparatedIntegerField(default='101162,102162,104162', max_length=70)),
                ('is_offered', models.BooleanField(default=False)),
                ('is_current_course', models.BooleanField(default=False)),
                ('credits', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(999)])),
                ('limit', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoursePlan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(help_text='Required. 5 characters or fewer. Uppercase Letters only. ', validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid course type code.', 'invalid')], max_length=5, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentCourse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(help_text='Required. 5 characters or fewer. Uppercase Letters only. ', validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid department code.', 'invalid')], max_length=5, unique=True)),
                ('name', models.CharField(help_text='Required. 50 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid department name.', 'invalid')], max_length=50, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DUGC',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('department', models.OneToOneField(to='oars.Department')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('min_semester', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('max_semester', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('min_cpi', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('filter_type', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('course', models.ForeignKey(to='oars.Course')),
                ('department', models.ForeignKey(null=True, to='oars.Department', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreviousCourse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('department', models.ForeignKey(to='oars.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Waiting'), (1, 'Accepted'), (2, 'Rejected'), (4, 'Waiting (limit exceeded)')], default=0)),
                ('added', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequestSubmit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Not submitted'), (1, 'Submitted'), (2, 'Submit & accepted'), (4, 'Submit & rejected')], default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('roll_no', models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('cpi', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='CPI')),
                ('department', models.ForeignKey(to='oars.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='requestsubmit',
            name='student',
            field=models.ForeignKey(to='oars.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='student',
            field=models.ForeignKey(to='oars.Student'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set([('course', 'student')]),
        ),
        migrations.AddField(
            model_name='previouscourse',
            name='student',
            field=models.ForeignKey(to='oars.Student'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='previouscourse',
            unique_together=set([('course', 'student')]),
        ),
        migrations.AddField(
            model_name='dugc',
            name='professor',
            field=models.OneToOneField(to='oars.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dugc',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='student',
            field=models.ForeignKey(to='oars.Student'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='currentcourse',
            unique_together=set([('course', 'student')]),
        ),
        migrations.AddField(
            model_name='courseplan',
            name='student',
            field=models.ForeignKey(to='oars.Student'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='courseplan',
            unique_together=set([('course', 'student')]),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(to='oars.CourseType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(to='oars.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, to='oars.Course', related_name='prerequisites_rel_+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to='oars.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='teaching_assistants',
            field=models.ManyToManyField(blank=True, null=True, to='oars.Student'),
            preserve_default=True,
        ),
    ]
