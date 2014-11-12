from django.conf.urls import patterns, include, url
from dugc import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^courses_offered/$', views.courses_offered, name='courses_offered'),
    url(r'^courses/(?P<course_id>\d+)/$', views.course, name='course'),
    url(r'^courses/(?P<course_id>\d+)/filters/$', views.course_filters, name='course_filters'),
    url(r'^courses/(?P<course_id>\d+)/waiting/$', views.students_waiting, name='students_waiting'),
    url(r'^courses/(?P<course_id>\d+)/accepted/$', views.students_accepted, name='students_accepted'),
    url(r'^courses/(?P<course_id>\d+)/rejected/$', views.students_rejected, name='students_rejected'),
    url(r'^course_listing/$', views.course_listing, name='course_listing'),
    url(r'^course_search/$', views.course_search, name='course_search'),
)