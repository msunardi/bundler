from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cause.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cause/', include('cause.urls', namespace='cause')),
 	url(r'^how/', TemplateView.as_view(template_name="how.html"), name='how'),
    url(r'^admin/', include(admin.site.urls)),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    	url(r'^profile_images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROFILE_IMAGES_ROOT}),
   )