from django.shortcuts import render

def home(request):
	return render(request, 'teca/home.html')

def help(request):
	return render(request, 'teca/help.html', {'title': 'Help'})



		