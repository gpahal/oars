from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^course_listing/$', views.course_listing, name='course_listing'),
    url(r'^course_search/$', views.course_search, name='course_search'),
    url(r'^course_request/$', views.course_request, name='course_request'),
)