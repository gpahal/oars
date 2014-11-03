from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated():
        return HttpResponse('Login successful')
    else:
        return HttpResponse('Not Logged in')