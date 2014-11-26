from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import ugettext_lazy as _

from oars.forms import UserCreationForm, UserChangeForm
from oars.models import (User, Department, Student, Professor, DUGC, CourseType,
                         Course, CurrentCourse, PreviousCourse, Request, CoursePlan, Filter)


class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'date_of_birth')}),
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
    list_display = ('username', 'email', 'full_name', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)
    filter_horizontal = ()


class StudentAdmin(admin.ModelAdmin):

    raw_id_fields = ('user', 'department')
    related_lookup_fields = {
        'fk': ['user', 'department'],
    }


class ProfessorAdmin(admin.ModelAdmin):

    raw_id_fields = ('user', 'department')
    related_lookup_fields = {
        'fk': ['user', 'department'],
    }


class DUGCAdmin(admin.ModelAdmin):

    raw_id_fields = ('user', 'department')
    related_lookup_fields = {
        'fk': ['user', 'department'],
    }


class CourseAdmin(admin.ModelAdmin):

    raw_id_fields = ('department', 'course_type',)
    autocomplete_lookup_fields = {
        'fk': ['department', 'course_type'],
    }
    filter_horizontal = ('professors', 'teaching_assistants', 'prerequisites')


class CurrentCourseAdmin(admin.ModelAdmin):

    raw_id_fields = ('course', 'student',)
    autocomplete_lookup_fields = {
        'fk': ['course', 'student'],
    }


class PreviousCourseAdmin(admin.ModelAdmin):

    raw_id_fields = ('course', 'student',)
    autocomplete_lookup_fields = {
        'fk': ['course', 'student'],
    }


class RequestAdmin(admin.ModelAdmin):

    raw_id_fields = ('course', 'student',)
    autocomplete_lookup_fields = {
        'fk': ['course', 'student'],
    }


class CoursePlanAdmin(admin.ModelAdmin):

    raw_id_fields = ('course', 'student',)
    autocomplete_lookup_fields = {
        'fk': ['course', 'student'],
    }


class FilterAdmin(admin.ModelAdmin):

    raw_id_fields = ('course', 'department',)
    autocomplete_lookup_fields = {
        'fk': ['course', 'department'],
    }

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(DUGC, DUGCAdmin)
admin.site.register(CourseType)
admin.site.register(Course, CourseAdmin)
admin.site.register(CurrentCourse, CurrentCourseAdmin)
admin.site.register(PreviousCourse, PreviousCourseAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(CoursePlan, CoursePlanAdmin)
admin.site.register(Filter, FilterAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)