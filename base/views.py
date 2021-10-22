from functools import update_wrapper
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
	template_name = 'base/login.html' 
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('notes')


class NoteList(LoginRequiredMixin, ListView):
	model = Note
	context_object_name = 'notes'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['notes'] = context['notes'].filter(user=self.request.user)
		return context

class NoteDetail(LoginRequiredMixin, DetailView):
	model = Note
	context_object_name = 'note'
	template_name = 'base/note.html'


class NoteCreate(LoginRequiredMixin, CreateView):
	model = Note
	fields = ['title', 'description']
	success_url = reverse_lazy('notes')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
	model = Note
	fields = ['title', 'description']
	success_url = reverse_lazy('notes')


class NoteDelete(LoginRequiredMixin, DeleteView):
	model = Note
	context_object_name = 'note'
	success_url = reverse_lazy('notes')
