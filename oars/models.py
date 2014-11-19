from django.conf import settings
from django.core.mail import send_mail
from django.core import validators
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_admin, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_admin=is_admin, is_active=True,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True,
                                 **extra_fields)


class User(AbstractBaseUser):
    """
    A class implementing a fully featured OARS User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """

    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
        ])

    email = models.EmailField(_('email address'))
    full_name = models.CharField(_('first name'), max_length=50, blank=True)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    is_admin = models.BooleanField(_('admin status'), default=False,
        help_text=_('Designates whether the user can log into the admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the full name.
        """

        if self.full_name == "":
            return self.username.capitalize()
        else:
            return self.full_name.capitalize()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """

        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        """
        Returns True only for active superusers
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_admin:
            return True

        # Otherwise return False.
        return False

    def has_perms(self, perm_list, obj=None):
        """
        Returns True only for active superusers
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_admin:
            return True

        # Otherwise return False.
        return False

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_admin:
            return True

        # Otherwise return False.
        return False

    @property
    def is_staff(self):
        """
        Returns True if the user is an admin
        """
        return self.is_admin


class Profile(models.Model):

    user = models.OneToOneField(User)
    user_type = settings.USER_NONE

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.get_username()

    def get_full_name(self):
        return self.user.get_full_name()


class Department(models.Model):

    code = models.CharField(max_length=5, unique=True,
        help_text=_('Required. 5 characters or fewer. Uppercase Letters only. '),
        validators=[
            validators.RegexValidator(r'^[A-Z]+$', _('Enter a valid department code.'), 'invalid'),
        ])
    name = models.CharField(max_length=50, unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits, spaces and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[ \w.@+-]+$', _('Enter a valid department name.'), 'invalid'),
        ])

    def __str__(self):
        return self.code


class Student(Profile):

    user_type = settings.USER_STUDENT
    department = models.ForeignKey(Department)
    roll_no = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
        ],
        unique=True,
    )
    semester = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(20),
        ],
    )
    cpi = models.DecimalField(_("CPI"), max_digits=4, decimal_places=2)


class Professor(Profile):

    user_type = settings.USER_PROFESSOR
    department = models.ForeignKey(Department)


class DUGC(Profile):

    user_type = settings.USER_DUGC
    department = models.OneToOneField(Department, unique=True)
    professor = models.OneToOneField(Professor)


class CourseType(models.Model):

    code = models.CharField(max_length=5, unique=True,
        help_text=_('Required. 5 characters or fewer. Uppercase Letters only. '),
        validators=[
            validators.RegexValidator(r'^[A-Z]+$', _('Enter a valid course type code.'), 'invalid'),
        ])

    def __str__(self):
        return self.code


class Course(models.Model):

    department = models.ForeignKey(Department)
    course_type = models.ForeignKey(CourseType)
    code = models.CharField(max_length=7,
        help_text=_('Required. 5 characters or fewer. Digits and uppercase letters only. '),
        validators=[
            validators.RegexValidator(r'^[A-Z]{2,3}[\d]{3}[A-Z]?$', _('Enter a valid course code.'), 'invalid'),
        ])
    name = models.CharField(max_length=50,
        help_text=_('Required. 50 characters or fewer. Letters, digits, spaces and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[ \w.@+-]+$', _('Enter a valid course name.'), 'invalid'),
        ])
    professors = models.ManyToManyField(Professor)
    prerequisites = models.ManyToManyField("self", blank=True)
    schedule = models.CommaSeparatedIntegerField(max_length=70, default='101162,102162,104162')
    is_offered = models.BooleanField(default=False)
    credits = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(100),
            validators.MaxValueValidator(999),
        ])
    limit = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
        ])

    def __str__(self):
        return self.code


class CurrentCourse(models.Model):

    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)

    class Meta:
        unique_together = (('course', 'student'),)

    def __str__(self):
        return "%s - %s" % (self.student, self.code)


class PreviousCourse(models.Model):

    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    grade = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10),
        ])

    class Meta:
        unique_together = (('course', 'student'),)

    def __str__(self):
        return "%s - %s" % (self.student, self.code)


class Request(models.Model):

    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    status = models.PositiveSmallIntegerField(choices=settings.REQUEST_STATUS_CHOICES, default=settings.WAITING)
    limit_exceeded = models.BooleanField(default=False)

    class Meta:
        unique_together = (('course', 'student'),)

    def __str__(self):
        return "%s - %s" % (self.student, self.course)

class CoursePlan(models.Model):

    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)

    class Meta:
        unique_together = (('course', 'student'),)

    def __str__(self):
        return "%s - %s" % (self.student, self.course)


class Filter(models.Model):

    course = models.ForeignKey(Course)
    department = models.ForeignKey(Department, blank=True, null=True)
    min_semester = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(20),
        ],
        blank=True,
        null=True,
    )
    max_semester = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(20),
        ],
        blank=True,
        null=True,
    )
    min_cpi = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10),
        ],
        blank=True,
        null=True,
    )
    # format: settings.ACCEPTED(1) for accept, settings.REJECTED(2) for reject,
    # [11-20] for preferences
    filter_type = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(20),
        ],
        blank=True,
        null=True,
    )