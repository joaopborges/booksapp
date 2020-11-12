from django.shortcuts import render
from .models import Post

posts = [
	{
		'author':'test',
		'title':'titletest',
		'content':'contenttest'

	},
	{
		'author':'errortest',
		'title':'errortesttitle',
		'content':'contenttesteerror'

	},
	{
		'author':'test2',
		'title':'titletest2',
		'content':'contenttest2'

	}
]




def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'teca/home.html', context)

def help(request):
	return render(request, 'teca/help.html', {'title': 'Help'})



		