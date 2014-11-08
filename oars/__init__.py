from oars.models import Department, CourseType, Course


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
    context = {
        'course_types': course_types,
        'courses': courses,
    }

    return context