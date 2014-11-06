from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def context_wrapper(request, context):

    context['usertype'] = 'Professor'
    context['user'] = request.user

    return context


def index(request):

    return HttpResponseRedirect(reverse('professor:profile'))


def profile(request, template_name='professor/profile.html'):

    context = context_wrapper(request, {})

    return TemplateResponse(request, template_name, context=context)