from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from oars import course_listing_context, course_search_context, course_request_context


def context_wrapper(request, context):

    context['usertype'] = 'Student'
    context['user'] = request.user

    return context


def index(request):

    return HttpResponseRedirect(reverse('student:profile'))


def profile(request, template_name='student/profile.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)


def course_listing(request, template_name='student/course_listing.html'):

    context = context_wrapper(request, course_listing_context())

    return TemplateResponse(request, template_name, context=context)


def course_search(request, template_name='student/course_search.html'):

    context = context_wrapper(request, course_search_context(request))

    return TemplateResponse(request, template_name, context=context)

def course_request(request, template_name='student/course_request.html'):

    context = context_wrapper(request, course_request_context(request))

    return TemplateResponse(request, template_name, context=context)