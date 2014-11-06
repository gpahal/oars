from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^course_search/$', views.course_search, name='course_search'),
    url(r'^course_listing/$', views.course_listing, name='course_listing'),
)