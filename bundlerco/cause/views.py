from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView

from cause.models import Cause, CauseForm

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
	return render(request, 'index.html')

class BaseView(View):
	"""Base, plain view"""
	pass

class BaseListView(ListView):
	page_sizes = (10, 20, 50)
	paginate_key = 'show'
	paginate_by = 10

	def get_paginate_by(self, queryset, **kwargs):
		return self.request.GET.get(self.paginate_key, self.paginate_by)

	def get_context_data(self, **kwargs):
		data = super(BaseListView, self).get_context_data(**kwargs)
		data['paginate_key'] = self.paginate_key
		data['page_sizes'] = self.page_sizes
		return data

class MainPageView(BaseListView):
	model = Cause
	template_name = 'index.html'
	#def get_context_data(self, **kwargs):
	#	data = super(MainPage, self).get_context_data(**kwargs)
	#	data['causes'] = self.causes
	#	return data

class CauseDetailView(DetailView):
	model = Cause
	template_name = 'cause_detail.html'

class CauseEditView(UpdateView):
	template_name = 'cause_form.html'
	model = Cause
	form_class = CauseForm
