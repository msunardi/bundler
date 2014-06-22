from django.conf.urls import patterns, include, url

from cause import views

urlpatterns = patterns('',
	url(r'^$', views.MainPageView.as_view(), name='index'),
	url(r'^detail/(?P<pk>\d+)/$', views.CauseDetailView.as_view(), name='detail'),
	url(r'^edit/(?P<pk>\d+)/$', views.CauseEditView.as_view(), name='edit'),
	#url(r'^create/(?<pk>\d+)/$', views.CauseCreateView.as_view(), name='create'),
)