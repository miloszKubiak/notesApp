from functools import update_wrapper
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView



class CustomLoginView(LoginView):
	template_name = 'base/login.html' 
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('notes')


class NoteList(ListView):
	model = Note
	context_object_name = 'notes'


class NoteDetail(DetailView):
	model = Note
	context_object_name = 'note'
	template_name = 'base/note.html'


class NoteCreate(CreateView):
	model = Note
	fields = '__all__'
	success_url = reverse_lazy('notes')


class NoteUpdate(UpdateView):
	model = Note
	fields = '__all__'
	success_url = reverse_lazy('notes')


class NoteDelete(DeleteView):
	model = Note
	context_object_name = 'note'
	success_url = reverse_lazy('notes')