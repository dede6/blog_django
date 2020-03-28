from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def hello_blog(request):
	lista = [
	'Django', 'Python', 'Git', 'HTML',
	 'DataBase', 'Nginx', 'Uwsgi', 'Systemctl'
	 ]

	list_post = Post.objects.filter(deleted= False)
	
	data = {'name' : 'Curso de Django 3', 
	'lista_tech' : lista,
	'post' : list_post
	}
	
	return render(request, 'index.html', data)

def post_detail(request, id):
	post = Post.objects.get(id=id)
	return render(request, 'post_detail.html', {'post' : post})