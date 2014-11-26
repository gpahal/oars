from oars.models import (Department, Student, Professor, CourseType, Course,
                         CurrentCourse, PreviousCourse, Request, Filter, CoursePlan)
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from decimal import Decimal
import itertools


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_filter_satisfied(request_obj, filter_obj):
    student = request_obj.student

    if filter_obj.department is not None and student.department != filter_obj.department:
        return False

    if filter_obj.min_semester is not None and student.semester < filter_obj.min_semester:
        return False

    if filter_obj.max_semester is not None and student.semester > filter_obj.max_semester:
        return False

    if filter_obj.min_cpi is not None and student.cpi < Decimal(filter_obj.min_cpi):
        return False

    return True


def apply_filter(request_obj, filter_obj):
    if not request_obj.course == filter_obj.course:
        return

    filter_type = int(filter_obj.filter_type)
    if filter_type == settings.REJECTED:
        request_obj.status = filter_type
    elif filter_type == settings.ACCEPTED:
        if request_obj.course.limit_exceeded():
            request_obj.status = filter_type
        else:
            request_obj.status = settings.WAITING_LE

    return


def course_requests_context(request):
    course_types = CourseType.objects.all()
    courses = Course.objects.filter(is_offered=True)

    if request.method == 'POST':
        is_new_request_submitted = request.POST.get('course_request', None)
        is_request_delete_submitted = request.POST.get('request_delete', None)
    else:
        is_new_request_submitted = False
        is_request_delete_submitted = False

    if is_new_request_submitted:
        course_code = request.POST.get('course_code', None)
        if course_code:
            course = Course.objects.get(id=course_code, is_offered=True)
            flag = True
            for prerequisite in course.prerequisites.all():
                count_previous = PreviousCourse.objects.filter(student=request.user.student, course=prerequisite).count()
                count_current = CurrentCourse.objects.filter(student=request.user.student, course=prerequisite).count()
                if count_previous + count_current == 0:
                    request_obj = Request(course=course, student=request.user.student, status=settings.REJECTED)
                    request_obj.save()
                    flag = False
                    break
            if flag:
                request_obj = Request(course=course, student=request.user.student, status=settings.WAITING)
                filters = Filter.objects.filter(course=course, filter_type__in=(settings.ACCEPTED, settings.REJECTED)).order_by('filter_type')
                for filter_obj in filters:
                    if is_filter_satisfied(request_obj, filter_obj):
                        apply_filter(request_obj, filter_obj)
                        break
                request_obj.save()

        else:
            raise ValidationError(
                _('Invalid course code'),
                code='invalid',
            )

    if is_request_delete_submitted:
        request_id = request.POST.get('request_id', None)
        if request_id:
            try:
                request_obj = Request.objects.get(id=request_id)
                request_obj.delete()
            except:
                raise ValidationError(
                    _('Invalid request id'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid request id'),
                code='invalid',
            )

    requests = Request.objects.filter(student=request.user.student)
    context = {
        'course_types': course_types,
        'courses': courses,
        'requests': requests,
        'WAITING': settings.WAITING,
        'ACCEPTED': settings.ACCEPTED,
        'REJECTED': settings.REJECTED,
    }

    return context

def course_submit_context(request):
    
    is_new_course_added = False
    is_course_delete_submitted = False
    if request.method == 'POST':
        is_new_course_added = request.POST.get('add_course', None)
        is_course_delete_submitted = request.POST.get('add_delete', None)
    else:
        is_new_course_added = False

    if is_new_course_added:
        request_id = request.POST.get('request_id', None)
        if request_id:
            request_obj = Request.objects.get(id=request_id)
            if request_obj.status == settings.ACCEPTED:
                request_obj.added = True
                request_obj.save()

    if is_course_delete_submitted:
        request_id = request.POST.get('request_id',None)
        if request_id:
            request_obj = Request.objects.get(id=request_id)
            request_obj.added = False
            request_obj.save()

    requests = Request.objects.filter(student=request.user.student,status=settings.ACCEPTED)
    added_courses = Request.objects.filter(student=request.user.student,added=True)
    context = {
        'requests' : requests,
        'courses' : added_courses,
    }
    return context

def course_plan_context(request):
    course_types = CourseType.objects.all()
    courses = Course.objects.filter(is_offered=True)

    if request.method == 'POST':
        is_new_request_submitted = request.POST.get('course_plan', None)
        is_request_delete_submitted = request.POST.get('request_delete', None)
    else:
        is_new_request_submitted = False
        is_request_delete_submitted = False

    if is_new_request_submitted:
        course_code = request.POST.get('course_code', None)
        if course_code:
            course = Course.objects.get(id=course_code, is_offered=True)
            request_obj = CoursePlan(course=course, student=request.user.student)
            request_obj.save()

        else:
            raise ValidationError(
                _('Invalid course code'),
                code='invalid',
            )

    if is_request_delete_submitted:
        request_id = request.POST.get('request_id', None)
        if request_id:
            try:
                request_obj = CoursePlan.objects.get(id=request_id)
                request_obj.delete()
            except:
                raise ValidationError(
                    _('Invalid request id'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid request id'),
                code='invalid',
            )

    requests = CoursePlan.objects.filter(student=request.user.student)
    context = {
        'course_types': course_types,
        'courses': courses,
        'requests': requests,
    }

    return context


def courses_offered_context(request):
    courses = Course.objects.select_related('professors').filter(professors__id=request.user.professor.id,
                                                                 is_offered=True)
    context = {
        'courses': courses,
    }

    return context


def courses_offered_dept_context(request):
    courses = Course.objects.select_related('department').filter(department=request.user.professor.department,
                                                                 is_offered=True)
    context = {
        'courses': courses,
    }

    return context


def course_context(course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {
        'course': course,
    }

    return context


def course_filters_context(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    departments = Department.objects.all()
    filters = Filter.objects.select_related('course').filter(course__id=course_id)

    if request.method == 'POST':
        is_new_filter_submitted = request.POST.get('course_filter', None)
        is_filter_delete_submitted = request.POST.get('filter_delete', None)
    else:
        is_new_filter_submitted = False
        is_filter_delete_submitted = False

    if is_new_filter_submitted:
        department = request.POST.get('department', None)
        if not department:
            department = None
        else:
            try:
                department = Department.objects.get(id=department)
            except Department.DoesNotExist:
                raise ValidationError(
                    _('Invalid department'),
                    code='invalid',
                )
        min_semester = request.POST.get('min_semester', None)
        if not min_semester:
            min_semester = None
        max_semester = request.POST.get('max_semester', None)
        if not max_semester:
            max_semester = None
        min_cpi = request.POST.get('min_cpi', None)
        if not min_cpi:
            min_cpi = None
        filter_type = request.POST.get('filter_type', None)

        if not filter_type:
            raise ValidationError(
                _('Invalid filter type'),
                code='invalid',
            )

        try:
            filter_obj = Filter(course=course, department=department, min_semester=min_semester,
                                max_semester=max_semester, min_cpi=min_cpi, filter_type=filter_type)
            requests = Request.objects.filter(course=course, status=settings.WAITING)
            if int(filter_type) in (settings.ACCEPTED, settings.REJECTED):
                for request_obj in requests:
                    if is_filter_satisfied(request_obj, filter_obj):
                        apply_filter(request_obj, filter_obj)
                        request_obj.save()
            filter_obj.save()
        except Exception as e:
            raise ValidationError(
                _(e.__str__()),
                code='invalid',
            )

    if is_filter_delete_submitted:
        filter_id = request.POST.get('filter_id', None)
        if filter_id:
            try:
                filter_obj = Filter.objects.get(id=filter_id, course=course)
                filter_obj.delete()
            except:
                raise ValidationError(
                    _('Invalid filter id'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid filter id'),
                code='invalid',
            )

    context = {
        'course': course,
        'departments': departments,
        'filters': filters,
        'WAITING': settings.WAITING,
        'ACCEPTED': settings.ACCEPTED,
        'REJECTED': settings.REJECTED,
    }

    return context


def course_filters_limited_context(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    departments = Department.objects.all()
    filters = Filter.objects.select_related('course').filter(course__id=course_id,
                                                             filter_type__in=(settings.ACCEPTED, settings.REJECTED))

    if request.method == 'POST':
        is_new_filter_submitted = request.POST.get('course_filter', None)
        is_filter_delete_submitted = request.POST.get('filter_delete', None)
    else:
        is_new_filter_submitted = False
        is_filter_delete_submitted = False

    if is_new_filter_submitted:
        department = request.POST.get('department', None)
        if not department:
            department = None
        else:
            try:
                department = Department.objects.get(id=department)
            except Department.DoesNotExist:
                raise ValidationError(
                    _('Invalid department'),
                    code='invalid',
                )
        min_semester = request.POST.get('min_semester', None)
        if not min_semester:
            min_semester = None
        max_semester = request.POST.get('max_semester', None)
        if not max_semester:
            max_semester = None
        min_cpi = request.POST.get('min_cpi', None)
        if not min_cpi:
            min_cpi = None
        filter_type = request.POST.get('filter_type', None)

        if not (filter_type and filter_type in (settings.ACCEPTED, settings.REJECTED)):
            raise ValidationError(
                _('Invalid filter type'),
                code='invalid',
            )

        try:
            filter_obj = Filter(course=course, department=department, min_semester=min_semester,
                                max_semester=max_semester, min_cpi=min_cpi, filter_type=filter_type)
            requests = Request.objects.filter(course=course, status=settings.WAITING)
            if int(filter_type) in (settings.ACCEPTED, settings.REJECTED):
                for request_obj in requests:
                    if is_filter_satisfied(request_obj, filter_obj):
                        apply_filter(request_obj, filter_obj)
                        request_obj.save()
            filter_obj.save()
        except Exception as e:
            raise ValidationError(
                _(e.__str__()),
                code='invalid',
            )

    if is_filter_delete_submitted:
        filter_id = request.POST.get('filter_id', None)
        if filter_id:
            try:
                filter_obj = Filter.objects.get(id=filter_id, course=course)
                filter_obj.delete()
            except:
                raise ValidationError(
                    _('Invalid filter id'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid filter id'),
                code='invalid',
            )

    context = {
        'course': course,
        'departments': departments,
        'filters': filters,
        'WAITING': settings.WAITING,
        'ACCEPTED': settings.ACCEPTED,
        'REJECTED': settings.REJECTED,
    }

    return context


def students_waiting_context(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    requests = Request.objects.filter(course_id=course_id,
                                      status__in=(settings.WAITING, settings.WAITING_LE)).order_by('id')
    filter_pref = Filter.objects.filter(filter_type__gte=10).order_by('filter_type')

    results = [[] for x in range(12)]

    if request.method == 'POST':
        is_selection_submitted = request.POST.get('selection_submit', None)
    else:
        is_selection_submitted = False

    if is_selection_submitted:
        for key, value in request.POST.items():
            if value == '1' or value == '0':
                if not is_number(key):
                    continue
                try:
                    request_obj = requests.get(id=key)
                    if request_obj.status == settings.WAITING:
                        if value == '1':
                            request_obj.status = settings.ACCEPTED
                            request_obj.save()
                        else:
                            request_obj.status = settings.REJECTED
                            request_obj.save()

                except Request.DoesNotExist:
                    raise ValidationError(
                        _('Invalid request id'),
                        code='invalid',
                    )
                except:
                    raise ValidationError(
                        _('Error while applying changes to request id'),
                        code='internal_error',
                    )

    for key in requests:
        if key.status == settings.WAITING_LE:
            results[0].append(key)
        else:
            flag = True
            for pref in filter_pref:
                if is_filter_satisfied(key, pref):
                    results[pref.filter_type - 10].append(key)
                    flag = False
                    break
            if flag:
                results[11].append(key)

    iterator = itertools.count(1).__next__
    context = {
        'course': course,
        'requests': requests,
        'request_count': len(requests),
        'results': results,
        'iterator': iterator,
    }
    return context


def students_accepted_context(course_id):
    course = get_object_or_404(Course, id=course_id)
    requests = Request.objects.filter(course_id=course_id, status=settings.ACCEPTED)
    context = {
        'course': course,
        'requests': requests,
    }

    return context


def students_rejected_context(course_id):
    course = get_object_or_404(Course, id=course_id)
    requests = Request.objects.filter(course_id=course_id, status=settings.REJECTED)
    context = {
        'course': course,
        'requests': requests,
    }

    return context


def course_listing_context():
    courses = Course.objects.filter(is_offered=True)
    context = {
        'courses': courses,
    }

    return context


def course_search_context(request):
    departments = Department.objects.all()
    course_types = CourseType.objects.all()
    courses = Course.objects.filter(is_offered=True)

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
            professors_1 = Professor.objects.filter(user__full_name__icontains=professor_name)
            professors_2 = Professor.objects.filter(user__username__icontains=professor_name)
            courses = courses.select_related('professors').filter(professors__in=(professors_1 | professors_2))
        if professor_email:
            professors = Professor.objects.filter(user__email__icontains=professor_email)
            courses = courses.select_related('professors').filter(professors__in=professors)

    context = {
        'departments': departments,
        'course_types': course_types,
        'courses': courses,
    }

    return context


def mailing_list_context(request):
    departments = Department.objects.all()
    emails = []
    display_emails = False
    department = None
    min_semester = None
    max_semester = None
    min_cpi = None
    email_self = "true"

    if request.method == 'POST':
        is_email_list_submitted = request.POST.get('get_email_list', None)
        is_send_message_submitted = request.POST.get('send_message', None)
    else:
        is_email_list_submitted = False
        is_send_message_submitted = False

    if is_email_list_submitted or is_send_message_submitted:
        students = Student.objects.all()
        department = request.POST.get('department', None)
        if department:
            try:
                department_obj = Department.objects.get(id=department)
                students = students.filter(department=department_obj)
            except Department.DoesNotExist:
                raise ValidationError(
                    _('Invalid department'),
                    code='invalid',
                )

        min_semester = request.POST.get('min_semester', None)
        if min_semester:
            students = students.filter(semester__gte=min_semester)

        max_semester = request.POST.get('max_semester', None)
        if max_semester:
            students = students.filter(semester__lte=max_semester)

        min_cpi = request.POST.get('min_cpi', None)
        if min_cpi:
            students = students.filter(cpi__gte=min_cpi)

        emails = [student.user.email for student in students]

        email_self = request.POST.get('email_self', None)
        if email_self == 'true':
            emails.append(request.user.email)

    if is_send_message_submitted:
        cc_to = request.POST.get('cc_to', None)
        if cc_to:
            cc_to = cc_to.replace(' ', '')
            cc_to = cc_to.split(',')
        else:
            cc_to = []

        bcc_to = request.POST.get('bcc_to', None)
        if bcc_to:
            bcc_to = bcc_to.replace(' ', '')
            bcc_to = bcc_to.split(',')
        else:
            bcc_to = []

        subject = request.POST.get('subject', None)
        if not subject:
            subject = ""

        message = request.POST.get('message', None)
        if not message:
            message = ""

        email_message = EmailMessage('From '+request.user.get_full_name()+': '+subject, message, request.user.email,
                                     emails, bcc=bcc_to, cc=cc_to)

        for attachment in request.FILES.getlist('attachments'):
            email_message.attach(attachment.name, attachment.read(), attachment.content_type)

        email_message.send()

    if is_email_list_submitted:
        display_emails = True

    context = {
        'departments': departments,
        'email_list': ', '.join(emails),
        'email_count': len(emails),
        'display_emails': display_emails,
        'department': department,
        'min_semester': min_semester,
        'max_semester': max_semester,
        'min_cpi': min_cpi,
        'email_self': (email_self == "true"),
    }

    return context