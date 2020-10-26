from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
	return HttpResponse ('<h1>Library home</h1>')

def help(request):
	return HttpResponse ('<h1>Help Center</h1>')


		