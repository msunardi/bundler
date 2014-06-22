from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django import http
from django.http import HttpResponseRedirect
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView, CreateView, FormMixin, ProcessFormView

from cause.models import Cause, CauseForm, Pledge, PledgeForm

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
	return render(request, 'index.html')

class BaseView(View):
	"""Base, plain view"""
	pass

class CauseListView(ListView):
	page_sizes = (10, 20, 50)
	paginate_key = 'show'
	paginate_by = 10
	queryset = Cause.objects.all().order_by('-created_date')
	template_name = 'cause_list.html'

	def get_paginate_by(self, queryset, **kwargs):
		return self.request.GET.get(self.paginate_key, self.paginate_by)

	def get_context_data(self, **kwargs):
		data = super(CauseListView, self).get_context_data(**kwargs)
		data['paginate_key'] = self.paginate_key
		data['page_sizes'] = self.page_sizes
		return data

class MainPageView(CauseListView):
	#model = Cause
	template_name = 'index.html'
	queryset = Cause.objects.all().order_by('-rating')[:3]
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

	def get_context_data(self, **kwargs):
		data = super(CauseEditView, self).get_context_data(**kwargs)
		data['page_title'] = 'Edit'
		return data

class CauseCreateView(CreateView):
	template_name = 'cause_form.html'
	model = Cause
	form_class = CauseForm
	success_url = reverse_lazy("cause:create-success")

	def get_context_data(self, **kwargs):
		data = super(CauseCreateView, self).get_context_data(**kwargs)
		data['page_title'] = 'Create'
		return data

	"""def get_success_url(self):
		if not hasattr(self, 'success_url') or self.success_url is None:
			self.success_url = self.request.path
		return super(CauseCreateView, self).get_success_url()

	def post(self, request, *args, **kwargs):
		self.object = None
		return super(CauseCreateView, self).post(request, *args, **kwargs)
	"""
	def form_valid(self, form):
		self.object = form.save()

		return HttpResponseRedirect(self.get_success_url())

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)

		if form.is_valid():
			return self.form_valid(form)
		return self.form_invalid(form)

	def get(self, request, *args, **kwargs):
		self.object = None
		return super(CauseCreateView, self).get(request, *args, **kwargs)

class CauseCreateSuccessView(BaseView):
	template_name = 'create_success.html'

class PledgeView(CreateView):
	template_name = 'pledge_form.html'
	model = Pledge
	form_class = PledgeForm
	success_url = reverse_lazy("cause:create-success")

	def get_context_data(self, **kwargs):
		data = super(PledgeView, self).get_context_data(**kwargs)
		data['cause'] = self.cause
		return data

	def get(self, request, *args, **kwargs):
		try:
			self.cause = Cause.objects.get(
                pk=long(kwargs.pop('pk'))
            )
		except (ValueError, KeyError, Cause.DoesNotExist):
			raise http.Http404
		return super(PledgeView, self).get(request, *args, **kwargs)


