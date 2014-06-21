from django.conf.urls import url

from cause import views

urlpatterns = [
	url(r'^$', views.MainPageView.as_view(), name='index')
]