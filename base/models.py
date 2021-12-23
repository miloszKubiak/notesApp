from django.db import models
from django.contrib.auth.models import User


#model notatki
class Note(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)#pole użytkownika z kluczem obcym i kaskadowym usuwaniem.
	title = models.CharField(max_length=200)#tytuł notatki.
	description = models.TextField(null=True, blank=True)#opis notatki czyli jej zawartość.
	create = models.DateTimeField(auto_now_add=True)#tworzenie notatki - data utworzenia.

#ustawiamy domyślną wartość na tytuł jako ciąg znaków(__str__).
	def __str__(self):
		return self.title


