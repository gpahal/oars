from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls', namespace='student')),
    url(r'^professor/', include('professor.urls', namespace='professor')),
    url(r'^dugc/', include('dugc.urls', namespace='dugc')),
    url(r'^', include('oars.urls')),
)