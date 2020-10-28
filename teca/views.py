from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
	return render(request, 'teca/home.html')

def help(request):
	return render(request, 'teca/help.html')



		