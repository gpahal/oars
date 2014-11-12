# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], unique=True, max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username')),
                ('email', models.EmailField(max_length=75, verbose_name='email address')),
                ('full_name', models.CharField(max_length=50, blank=True, verbose_name='first name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('is_admin', models.BooleanField(default=False, help_text='Designates whether the user can log into the admin site.', verbose_name='admin status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(validators=[django.core.validators.RegexValidator('^[A-Z]{2,3}[\\d]{3}[A-Z]?$', 'Enter a valid course code.', 'invalid')], max_length=7, help_text='Required. 5 characters or fewer. Digits and uppercase letters only. ')),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid course name.', 'invalid')], max_length=50, help_text='Required. 50 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.')),
                ('is_offered', models.BooleanField(default=False)),
                ('credits', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(999)])),
                ('limit', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid course type code.', 'invalid')], unique=True, max_length=5, help_text='Required. 5 characters or fewer. Uppercase Letters only. ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid department code.', 'invalid')], unique=True, max_length=5, help_text='Required. 5 characters or fewer. Uppercase Letters only. ')),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid department name.', 'invalid')], unique=True, max_length=50, help_text='Required. 50 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DUGC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('min_semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], blank=True, null=True)),
                ('max_semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], blank=True, null=True)),
                ('min_cpi', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], blank=True, null=True)),
                ('filter_type', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], blank=True, null=True)),
                ('course', models.ForeignKey(to='oars.Course')),
                ('department', models.ForeignKey(to='oars.Department', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreviousCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Waiting'), (1, 'Accepted'), (2, 'Rejected')], default=0)),
                ('limit_exceeded', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('roll_no', models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('cpi', models.DecimalField(max_digits=4, verbose_name='CPI', decimal_places=2)),
                ('department', models.ForeignKey(to='oars.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
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
    ]
