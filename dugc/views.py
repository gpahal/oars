from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from oars import course_listing_context, course_search_context

def context_wrapper(request, context):

    context['usertype'] = 'DUGC'
    context['user'] = request.user

    return context


def index(request):

    return HttpResponseRedirect(reverse('dugc:profile'))


def profile(request, template_name='dugc/profile.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)


def course_listing(request, template_name='dugc/course_listing.html'):

    context = context_wrapper(request, course_listing_context())

    return TemplateResponse(request, template_name, context=context)


def course_search(request, template_name='dugc/course_search.html'):

    context = context_wrapper(request, course_search_context(request))

    return TemplateResponse(request, template_name, context=context)