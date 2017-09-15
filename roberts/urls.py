from __future__ import unicode_literals
from django.conf.urls import url
from . import views
from watson.views import search, search_json

urlpatterns = [
	# Home page
	url(r'^$', views.index, name='index'),
	#Todas las categorias
	url(r'^categorias/$', views.categorias, name='categorias'),
	url(r'^categoria/(?P<categoria_id>\d+)/$', views.categoria, name='categoria'),  
	url(r'^contenido/(?P<tema_id>\d+)/$',views.contenido, name='contenido'),
	url(r'^contenidos/$',views.contenidos, name='contenidos'),
	url(r'^contenidos/(?P<contenido_id>\d+)/$',views.contenidos, name='contenidos'),
	url(r'^new_content/$',views.new_content, name='new_content'),
	url(r'^new_tema/$',views.new_tema, name='new_tema'),
	# Todos los temas
	url(r'^temas/$',views.temas, name='temas'),
	url(r'^lista_contenidos/$',views.lista_contenidos, name='lista_contenidos'),
	url(r'^tema/(?P<tema_id>\d+)/$',views.tema, name='tema'),
    #url(r'^search_results/$', views.search_results, name='search_results'),
    #url("^json/$", search_json, name="search_json"),
	#url(r'^rb_search_list_view/$', views.rb_search_list_view, name='rb_search_list_view'),

]