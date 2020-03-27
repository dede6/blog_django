from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_blog(request):
	lista = [
	'Django', 'Python', 'Git', 'HTML',
	 'DataBase', 'Nginx', 'Uwsgi', 'Systemctl'
	 ]
	data = {'name' : 'Curso de Django 3', 'lista_tech' : lista}
	return render(request, 'index.html', data)