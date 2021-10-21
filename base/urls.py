from django.urls import path
from .views import NoteList

urlpatterns = [
  path('', NoteList.as_view(), name='notes'),
]