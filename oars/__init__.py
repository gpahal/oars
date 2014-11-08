from oars.models import Department, CourseType, Course, Request
from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _

def course_listing_context():

    courses = Course.objects.all()
    context = {
        'courses': courses,
    }

    return context


def course_search_context(request):

    departments = Department.objects.all()
    course_types = CourseType.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        is_form_submitted = request.POST.get('course_search', None)
    else:
        is_form_submitted = False

    if is_form_submitted:
        course_type = request.POST.get('course_type', None)
        code = request.POST.get('code', None)
        department = request.POST.get('department', None)
        name = request.POST.get('name', None)
        professor_name = request.POST.get('professor_name', None)
        professor_email = request.POST.get('professor_email', None)

        if course_type:
            courses = courses.filter(course_type__id=course_type)
        if code:
            courses = courses.filter(code__icontains=code)
        if department:
            courses = courses.filter(department__id=department)
        if name:
            courses = courses.filter(name__icontains=name)
        if professor_name:
            courses = courses.filter(professors__user__get_full_name__icontains=professor_name)
        if professor_email:
            courses = courses.filter(professors__user__email__icontains=professor_email)


    context = {
        'departments': departments,
        'course_types': course_types,
        'courses': courses,
    }

    return context

def course_request_context(request):

    course_types = CourseType.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        is_new_request_submitted = request.POST.get('course_request', None)
        is_request_delete_submitted = request.POST.get('request_delete', None)
    else:
        is_new_request_submitted = False
        is_request_delete_submitted = False

    if is_new_request_submitted:
        course_code = request.POST.get('course_code', None)
        if course_code:
            course = Course.objects.get(pk=course_code)
            request = Request(course=course, student=request.user.student, status=settings.WAITING)
            request.save()
        else:
            raise forms.ValidationError(
                    _('Invalid value'),
                    code='invalid',
            )

    if is_request_delete_submitted:
        request_id = request.POST.get('request_id', None)
        if request_id:
            request = Request.objects.get(pk=request_id)
            request.delete()
        else:
            raise forms.ValidationError(
                    _('Invalid value'),
                    code='invalid',
            )

    requests = Request.objects.filter(student=request.user.student)
    context = {
        'course_types': course_types,
        'courses': courses,
        'requests': requests,
        'WAITING' : settings.WAITING,
        'ACCEPTED' : settings.ACCEPTED,
        'REJECTED' : settings.REJECTED,
    }

    return context