from django import forms
from .models import Contenido, Tema, Categoria
from tinymce.widgets import TinyMCE

class TemaForm(forms.ModelForm):
	class Meta:
		model = Tema
		categoria = {'categoria': forms.ModelChoiceField(queryset=Categoria.objects.all())}
		fields = ['categoria','text']
		Labels = {'text': ''}
		

class ContentForm(forms.ModelForm):
	class Meta:
		model = Contenido
		tema = {'tema': forms.ModelChoiceField(queryset=Tema.objects.all())}
		fields = ['tema','titulo', 'script']
		Labels = {'titulo': ''}
		#widgets = {'script': forms.Textarea(attrs={'cols':80})}
		script = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))


