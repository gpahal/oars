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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=75, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('date_of_birth', models.DateField(null=True, blank=True, verbose_name='date of birth')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid course type code.', 'invalid')], help_text='Required. 5 characters or fewer. Uppercase Letters only. ', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(to='oars_auth.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[A-Z]+$', 'Enter a valid department code.', 'invalid')], help_text='Required. 5 characters or fewer. Uppercase Letters only. ', unique=True)),
                ('name', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid department name.', 'invalid')], help_text='Required. 25 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DUGC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.OneToOneField(to='oars_auth.Department')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreviousCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('course', models.ForeignKey(to='oars_auth.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(to='oars_auth.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('cpi', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='CPI')),
                ('department', models.ForeignKey(to='oars_auth.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='previouscourse',
            name='student',
            field=models.ForeignKey(to='oars_auth.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dugc',
            name='professor',
            field=models.OneToOneField(to='oars_auth.Professor'),
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
            field=models.ForeignKey(to='oars_auth.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(to='oars_auth.CourseType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(to='oars_auth.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(to='oars_auth.Course', related_name='prerequisites_rel_+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to='oars_auth.Professor'),
            preserve_default=True,
        ),
    ]
