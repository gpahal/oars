from django.conf.urls import patterns, include, url
from django.contrib import admin
from oars import course_allocation

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(course_allocation.urls, namespace="ca")),
)
