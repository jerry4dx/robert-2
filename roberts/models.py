from django.db import models


# Create your models here.
class Categoria(models.Model):
	"""las categorias en las que se clasifican los topicos"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string of the model"""
		return self.text


class Tema(models.Model):
	"""Temas para cada proceso"""
	categoria = models.ForeignKey(Categoria)
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'temas'
			

	def __str__(self):
		"""Return a string of the model"""
		return self.text

class Contenido(models.Model):
	"""Los procesos documentados"""
	tema = models.ForeignKey(Tema)
	titulo = models.CharField(max_length=100)
	script = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'contenidos'

	def get_absolute_url(self):
		return "/contenido/%i/" % self.id

	def __unicode__(self):
		return unicode(self.tema)

	def __str__(self):
		return self.titulo
