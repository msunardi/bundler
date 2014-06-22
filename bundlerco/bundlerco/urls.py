from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cause.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cause/', include('cause.urls', namespace='cause')),
 	url(r'^how/', TemplateView.as_view(template_name="how.html"), name='how'),
    url(r'^admin/', include(admin.site.urls)),
)
