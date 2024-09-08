# Importa o módulo admin do Django para gerenciar o site de administração
from django.contrib import admin
# Importa a função path do módulo django.urls para definir rotas URL
from django.urls import path
# Importa a classe PostView do módulo blog.views para associar a uma rota URL
from blog.views import PostView

# Lista de padrões de URL para o projeto
urlpatterns = [
    # Rota para a interface de administração do Django
    path('admin/', admin.site.urls),
    # Rota para a view PostView, acessível via /home
    path('home/', PostView.as_view(), name='home-view'),  # Rota /home para a PostView
]
