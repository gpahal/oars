from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from oars import course_listing_context, course_search_context, course_requests_context, course_plan_context, course_submit_context


def context_wrapper(request, context):
    context['usertype'] = 'Student'
    context['user'] = request.user

    return context


def index(request):
    return HttpResponseRedirect(reverse('student:profile'))


def profile(request, template_name='student/profile.html'):
    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)


def course_requests(request, template_name='student/course_requests.html'):
    context = context_wrapper(request, course_requests_context(request))

    return TemplateResponse(request, template_name, context=context)


def course_plan(request, template_name='student/course_plan.html'):
    context = context_wrapper(request, course_plan_context(request))

    return TemplateResponse(request, template_name, context=context)


def course_listing(request, template_name='student/course_listing.html'):
    context = context_wrapper(request, course_listing_context())

    return TemplateResponse(request, template_name, context=context)


def course_search(request, template_name='student/course_search.html'):
    context = context_wrapper(request, course_search_context(request))

    return TemplateResponse(request, template_name, context=context)

def course_submit(request, template_name='student/course_submit.html'):
    context = context_wrapper(request, course_submit_context(request))

    return TemplateResponse(request, template_name, context=context)