from django.urls import path
from .views import NoteDelete, NoteList, NoteDetail, NoteCreate, NoteUpdate, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

#tutaj mamy ścieżki, które przekierowują nas z "kontrolerów" do poszczególnych widoków.
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),#logowanie użytkownika.
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),#widok po wylogowaniu.
    path('register/', RegisterPage.as_view(), name='register'),#rejestracja użytkownika.
    path('', NoteList.as_view(), name='notes'),#lista notatek.
    path('note/<int:pk>/', NoteDetail.as_view(), name='note'),#podgląd notatki.
    path('note-create/', NoteCreate.as_view(), name='note-create'),#tworzenie notatki.
    path('note-update/<int:pk>', NoteUpdate.as_view(), name='note-update'),#edycja notatki.
    path('note-delete/<int:pk>', NoteDelete.as_view(), name='note-delete'),#usuwanie notatki.
]
