from django.conf.urls import patterns, include, url
from django.contrib import admin
import course_allocation

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('oars_auth.urls')),
    url(r'^', include('course_allocation.urls', namespace="ca")),
)