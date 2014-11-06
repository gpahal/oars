# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('email', models.EmailField(max_length=75, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('date_of_birth', models.DateField(null=True, blank=True, verbose_name='date of birth')),
                ('is_admin', models.BooleanField(help_text='Designates whether the user can log into the admin site.', verbose_name='admin status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[\\d]{3}[A-Z]?$', 'Enter a valid course code.', 'invalid')], help_text='Required. 5 characters or fewer. Digits and uppercase letters only. ')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid course name.', 'invalid')], help_text='Required. 50 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.')),
                ('is_offered', models.BooleanField(default=False)),
                ('credits', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(999)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid course type code.', 'invalid')], help_text='Required. 5 characters or fewer. Uppercase Letters only. ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('course', models.ForeignKey(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid department code.', 'invalid')], help_text='Required. 5 characters or fewer. Uppercase Letters only. ')),
                ('name', models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid department name.', 'invalid')], help_text='Required. 25 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DUGC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('department', models.OneToOneField(to='oars.Department')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreviousCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Waiting'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('course', models.OneToOneField(to='oars.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('cpi', models.DecimalField(verbose_name='CPI', max_digits=4, decimal_places=2)),
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
            field=models.OneToOneField(to='oars.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='previouscourse',
            name='student',
            field=models.ForeignKey(to='oars.Student'),
            preserve_default=True,
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
            field=models.ManyToManyField(to='oars.Course', related_name='prerequisites_rel_+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to='oars.Professor'),
            preserve_default=True,
        ),
    ]
