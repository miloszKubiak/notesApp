from functools import update_wrapper
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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