from django.conf.urls import patterns, include, url
from dugc import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
)