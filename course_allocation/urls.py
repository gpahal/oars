from django.conf.urls import patterns, include, url

from course_allocation import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(course_allocation.urls, namespace="ca")),
    url(r'^$', views.home, name='home'),
)