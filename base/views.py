from django.shortcuts import render
from django.http import HttpResponse

def noteList(request):
  return HttpResponse('My Notes')