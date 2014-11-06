from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from oars.models import Course

def context_wrapper(request, context):

    context['usertype'] = 'Student'
    context['user'] = request.user

    return context


def index(request):

    return HttpResponseRedirect(reverse('student:profile'))


def profile(request, template_name='student/profile.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)

def course_search(request, template_name='student/course_search.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)

def course_listing(request, template_name='student/course_listing.html'):

    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    context = context_wrapper(request, context)
    return TemplateResponse(request, template_name, context=context)