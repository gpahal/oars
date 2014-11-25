from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from oars import (courses_offered_context, course_context,
                  students_waiting_context, students_accepted_context, students_rejected_context,
                  course_filters_context, course_listing_context, course_search_context, mailing_list_context)


def context_wrapper(request, context):
    context['usertype'] = 'Professor'
    context['user'] = request.user

    return context


def index(request):
    return HttpResponseRedirect(reverse('professor:profile'))


def profile(request, template_name='professor/profile.html'):
    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)


def courses_offered(request, template_name='professor/courses_offered.html'):
    context = context_wrapper(request, courses_offered_context(request))

    return TemplateResponse(request, template_name, context=context)


def course(request, course_id=None, template_name='professor/course.html'):
    context = context_wrapper(request, course_context(course_id))

    return TemplateResponse(request, template_name, context=context)


def course_filters(request, course_id=None, template_name='professor/course_filters.html'):
    context = context_wrapper(request, course_filters_context(request, course_id))

    return TemplateResponse(request, template_name, context=context)


def students_waiting(request, course_id=None, template_name='professor/students_waiting.html'):
    context = context_wrapper(request, students_waiting_context(request, course_id))

    return TemplateResponse(request, template_name, context=context)


def students_accepted(request, course_id=None, template_name='professor/students_accepted.html'):
    context = context_wrapper(request, students_accepted_context(course_id))

    return TemplateResponse(request, template_name, context=context)


def students_rejected(request, course_id=None, template_name='professor/students_rejected.html'):
    context = context_wrapper(request, students_rejected_context(course_id))

    return TemplateResponse(request, template_name, context=context)


def course_listing(request, template_name='professor/course_listing.html'):
    context = context_wrapper(request, course_listing_context())

    return TemplateResponse(request, template_name, context=context)


def course_search(request, template_name='professor/course_search.html'):
    context = context_wrapper(request, course_search_context(request))

    return TemplateResponse(request, template_name, context=context)


def mailing_list(request, template_name='professor/mailing_list.html'):
    context = context_wrapper(request, mailing_list_context(request))

    return TemplateResponse(request, template_name, context=context)