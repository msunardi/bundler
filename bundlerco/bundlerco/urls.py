from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cause.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('cause.urls', namespace='cause')),
    url(r'^admin/', include(admin.site.urls)),
)
