from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def context_wrapper(request, context):

    context['usertype'] = 'Student'
    context['user'] = request.user

    return context


def index(request):

    return HttpResponseRedirect(reverse('student:profile'))


def profile(request, template_name='student/profile.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)