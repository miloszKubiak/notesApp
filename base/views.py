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

#przyjmijmy na samym początku, że klasy, które są poniżej będe nazywać kontrolerami ponieważ spełniają wg mnie taką samą funkcje co kontrolery w innych frameworkach np. Laravel, tylko są zapisane dużo prościej niż w innych językach :)

#tworzenie kontrolera do widoku logowania.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

#jeśli logowanie się powiedzie, zostaniemy przekierowani do widoku listy notatek, który przyjmuje nazwę "notes".
    def get_success_url(self):
        return reverse_lazy('notes')


#tworzenie kontrolera do widoku rejestracji.
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm 
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

#walidacja użytkownika, jeśli rejestracja przejdzie pomyslnie, zostanie zalogowany, w innym przypadku zostanie z powrotem przekierowany na strone rejestracji.
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

#kontroler odpowiedzialny za listę notatek.
class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'

#funkcja, która zapewni nam, że użytkownik w liście notatek będzie widzieć tylko własne dane. Dzięki **kwargs możemy przyjąć za argument parametry klucz:wartość.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)

#możliwość wyszukiwania notatek, filtrujemy wyniki wyszukiwania po wpisanej frazie także wystarczy jesli znamy dowolną część tytułu notatki.
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['notes'] = context['notes'].filter(
                title__icontains=search_input) 

        context['search_input'] = search_input

        return context

#kontroler odpowiedzialny za samą możliwość podglądu notatki.
class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'base/note.html'

#kontroler odpowiedzialny za tworzenie notatki.
class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'description']
    success_url = reverse_lazy('notes')

#walidacja - jeśli użytkownik ją przejdzie to będzie mógł utworzyć notatkę.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)

#kontroler odpowiedzialny za edycję notatki.
class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'description']
    success_url = reverse_lazy('notes')
    template_name = 'base/note-edit.html'

#kontroler odpowiedzialny za usuwanie notatki.
class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')

#może nie zawsze potrafię wszystko dobrze wytłumaczyć, ale starałem się o to żeby komentarze były przejrzyste :)