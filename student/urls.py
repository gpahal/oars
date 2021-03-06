from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^course_requests/$', views.course_requests, name='course_requests'),
                       url(r'^course_plan/$', views.course_plan, name='course_plan'),
                       url(r'^course_listing/$', views.course_listing, name='course_listing'),
                       url(r'^course_search/$', views.course_search, name='course_search'),
                       url(r'^course_submit/$', views.course_submit, name='course_submit'),
                       )