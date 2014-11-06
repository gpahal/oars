from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import ugettext_lazy as _

from oars.forms import UserCreationForm, UserChangeForm
from oars.models import (User, Department, Student, Professor, DUGC,
                         CourseType, Course, CurrentCourse, PreviousCourse)


class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',),
        }),
        (_('Permissions'), {
            'classes': ('wide',),
            'fields': ('is_admin',),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(DUGC)
admin.site.register(CourseType)
admin.site.register(Course)
admin.site.register(CurrentCourse)
admin.site.register(PreviousCourse)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)