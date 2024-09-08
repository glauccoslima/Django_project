# Importa a classe HttpResponse do módulo django.http para criar respostas HTTP
from django.http import HttpResponse
# Importa a classe View do módulo django.views para criar views baseadas em classes
from django.views import View

# Define uma classe PostView que herda de View
class PostView(View):
    # Define um método GET para a classe PostView
    @staticmethod  # Converte o método em um método estático, pois não usa a instância da classe
    def get(request):
        # Retorna uma resposta HTTP com o texto "Hello World!"
        return HttpResponse("Hello World!")
