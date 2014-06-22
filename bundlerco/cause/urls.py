from django.conf.urls import patterns, include, url

from cause import views

urlpatterns = patterns('',
	url(r'^$', views.MainPageView.as_view(), name='index'),
	url(r'^list/$', views.CauseListView.as_view(), name='list'),
	url(r'^detail/(?P<pk>\d+)/$', views.CauseDetailView.as_view(), name='detail'),
	url(r'^edit/(?P<pk>\d+)/$', views.CauseEditView.as_view(), name='edit'),
	url(r'^create/$', views.CauseCreateView.as_view(), name='create'),
	url(r'^createsuccess/$', views.CauseCreateSuccessView.as_view(), name='create-success'),

	url(r'^pledge/(?P<pk>\d+)/$', views.PledgeView.as_view(), name='pledge'),
)