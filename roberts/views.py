from django.views import generic
from django.shortcuts import render
from watson import search as watson
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import operator

from django.db.models import Q

from .models import Contenido, Categoria, Tema
from .forms import ContentForm, TemaForm
# Create your views here.
def index(request):
	"""Robert's Home Page"""
	categoria = Categoria.objects.order_by('date_added')
	return render(request, 'roberts/index.html')

def categorias(request):
	cats = Categoria.objects.order_by('date_added')
	context= {'categorias': cats}
	return render(request, 'roberts/categorias.html', context)

def categoria(request, categoria_id):
	""" Muestra 1 categoria y sus temas"""
	cat = Categoria.objects.get(id=categoria_id)
	tema = cat.tema_set.order_by('-date_added')
	context= {'categoria': cat, 'tema': tema}
	return render(request, 'roberts/categoria.html', context)

def temas(request):
	"""ver LISTA DE temas"""
	temas = Tema.objects.order_by('-date_added')
	context = {'temas': temas}
	return render(request, 'roberts/temas.html', context)

def contenidos(request, tema_id):
	"""ver contenidos"""
	tema = Tema.objects.get(id=tema_id)
	content = Contenido.objects.order_by('titulo')
	context = {'contenidos': content, 'tema': tema}
	return render(request, 'roberts/contenidos.html', context)

def contenido(request, tema_id):
	"""Muestra un solo tema y sus contenidos"""
	tema = Tema.objects.get(id=tema_id)
	contents = tema.contenido_set.order_by('-date_added')
	context = {'contents': contents, 'tema': tema}
	return render(request, 'roberts/contenido.html', context)

def lista_contenidos(request):
	"""ver lista de contenidos"""
	
	content = Contenido.objects.order_by('-date_added')
	context = {'contenidos': content}
	return render(request, 'roberts/lista_contenidos.html', context)

#def search_results(request):
#	search_results= watson.search("Search terms")
#	return render(request, 'roberts/search_results.html')

def new_tema(request):
	""" Add new tema"""
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = TemaForm()
	else:
		form = TemaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('roberts:temas'))

	context = {'form': form}
	return render(request, 'roberts/new_tema.html', context)


def new_content(request):
	""" Add new content for a tema"""
	#tema = Tema.objects.get(id=tema_id)
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = ContentForm()
	else:
		form = ContentForm(request.POST)
		if form.is_valid():
			form.save()
			#new_content = form.save(commit=False)
			#new_content.tema = tem
			#new_content.save()
			return HttpResponseRedirect(reverse('roberts:lista_contenidos'))

	context = {'form': form}
	return render(request, 'roberts/new_content.html', context)

def tema(request, tema_id):
	""" Ver un tema y sus procesos"""
	tema = Tema.objects.get(id=tema_id)
	contenidos = tema.contenido_set.order_by('-date_added')
	context ={'tema':tema, 'contenidos': contenidos}
	return render(request,'roberts/tema.html', context)



		

