from django.conf.urls import patterns, url

from oars import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^logout/$', views.logout, name='logout'),
                       url(r'^logout_then_login/$', views.logout_then_login, name='logout_then_login'),
                       url(r'^password_change/$', views.password_change, name='password_change'),
                       url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
                       url(r'^password_reset/$', views.password_reset, name='password_reset'),
                       url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                           views.password_reset_confirm,
                           name='password_reset_confirm'),
                       url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
                       url(r'^common/course/(?P<course_id>\d+)/', views.course, name='course'),
                       )
