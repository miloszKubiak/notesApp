from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Note

class NoteList(ListView):
	model = Note
	context_object_name = 'notes'