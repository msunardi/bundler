from django.conf.urls import patterns, include, url

from cause import views

urlpatterns = patterns('',
	url(r'^$', views.MainPageView.as_view(), name='index'),
	url(r'^detail/(?P<pk>\d+)/$', views.CauseDetailView.as_view(), name='detail'),
)