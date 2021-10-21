from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.detail import DetailView



class NoteList(ListView):
	model = Note
	context_object_name = 'notes'


class NoteDetail(DetailView):
	model = Note
	context_object_name = 'note'
	template_name = 'base/note.html'