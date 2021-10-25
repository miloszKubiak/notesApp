from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
	template_name = 'base/login.html' 
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('notes')


class RegisterPage(FormView):
	template_name = 'base/register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('notes')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterPage, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('notes')
		return super(RegisterPage, self).get(*args, **kwargs)


class NoteList(LoginRequiredMixin, ListView):
	model = Note
	context_object_name = 'notes'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['notes'] = context['notes'].filter(user=self.request.user)

		search_input = self.request.GET.get('search-area') or ''
		if search_input:
			context['notes'] = context['notes'].filter(title__icontains=search_input)
			# title__startswith - if we want to filter from the first letter
		
		context['search_input'] = search_input

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
	template_name = 'base/note-edit.html'


class NoteDelete(LoginRequiredMixin, DeleteView):
	model = Note
	context_object_name = 'note'
	success_url = reverse_lazy('notes')
