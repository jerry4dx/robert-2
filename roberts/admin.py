from django.contrib import admin

# Register your models here.
from roberts.models import Categoria, Tema, Contenido

list_display = ['__unicode__', '__str__']

admin.site.register(Categoria)
admin.site.register(Tema)
admin.site.register(Contenido)
