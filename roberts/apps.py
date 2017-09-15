from django.apps import AppConfig
from watson import search as watson

class RobertsConfig(AppConfig):
    name = 'roberts'

    def ready(self):
        Contenido = self.get_model('Contenido')

        watson.register(Contenido, fields=("tema", "titulo"))



