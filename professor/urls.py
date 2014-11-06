from django.conf.urls import patterns, include, url
from professor import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
)