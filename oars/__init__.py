from oars.models import Department, Student, Professor, CourseType, Course, Request, Filter
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from decimal import Decimal


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

    if int(filter_obj.filter_type) in (settings.ACCEPTED, settings.REJECTED):
        request_obj.status = filter_obj.filter_type
    request_obj.save()

    return


def course_requests_context(request):

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
            course = Course.objects.get(code=course_code)
            request_obj = Request(course=course, student=request.user.student, status=settings.WAITING)
            filters = Filter.objects.filter(course=course, filter_type__in=(settings.ACCEPTED, settings.REJECTED))
            for filter_obj in filters:
                if is_filter_satisfied(request_obj, filter_obj):
                    apply_filter(request_obj, filter_obj)
                    break
        else:
            raise ValidationError(
                _('Invalid value'),
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
                    _('Invalid value'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid value'),
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


def courses_offered_context(request):

    courses = Course.objects.select_related('professors').filter(professors__id=request.user.professor.id)
    context = {
        'courses': courses,
    }

    return context


def courses_offered_dept_context(request):

    courses = Course.objects.select_related('department').filter(department=request.user.professor.department)
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
                    _('Invalid value'),
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
            for request_obj in requests:
                if is_filter_satisfied(request_obj, filter_obj):
                    apply_filter(request_obj, filter_obj)
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
                    _('Invalid value'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid value'),
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
                    _('Invalid value'),
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
            for request_obj in requests:
                if is_filter_satisfied(request_obj, filter_obj):
                    apply_filter(request_obj, filter_obj)
            filter_obj.save()
        except:
            raise ValidationError(
                _('Invalid value'),
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
                    _('Invalid value'),
                    code='invalid',
                )
        else:
            raise ValidationError(
                _('Invalid value'),
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
    requests = Request.objects.filter(course_id=course_id, status=settings.WAITING)

    context = {
        'course': course,
        'requests': requests,
    }

    if request.method == 'POST':
        is_number_selection_accept_submitted = request.POST.get('selection_number_accept', None)
        is_number_selection_reject_submitted = request.POST.get('selection_number_reject', None)
        is_selection_submitted = request.POST.get('selection_submit', None)
    else:
        is_number_selection_accept_submitted = False
        is_number_selection_reject_submitted = False
        is_selection_submitted = False

    if is_number_selection_accept_submitted or is_number_selection_reject_submitted:
        selection_type = request.POST.get('selection_type', None)
        selection_number = request.POST.get('selection_number', None)

        if selection_type and selection_number:
            # selct the top 'selection_number' from 'selection_type' based on list sorted by preferences
            pass

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
                # except:
                #     raise ValidationError(
                #         _('Error while applying changes to request id'),
                #         code='internal_error',
                #     )

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