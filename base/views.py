from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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