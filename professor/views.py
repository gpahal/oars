from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from oars import course_listing_context, course_search_context

def context_wrapper(request, context):

    context['usertype'] = 'Professor'
    context['user'] = request.user

    return context


def index(request):

    return HttpResponseRedirect(reverse('professor:profile'))


def profile(request, template_name='professor/profile.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)


def course_listing(request, template_name='professor/course_listing.html'):

    context = context_wrapper(request, course_listing_context())

    return TemplateResponse(request, template_name, context=context)


def course_search(request, template_name='professor/course_search.html'):

    context = context_wrapper(request, course_search_context(request))

    return TemplateResponse(request, template_name, context=context)

# def course_filter(request, course_id=None)

def course_filters(request, template_name='professor/course_filters.html'):

    context = context_wrapper(request, course_search_context(request))

    return TemplateResponse(request, template_name, context=context)