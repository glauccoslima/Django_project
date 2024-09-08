from django.contrib import admin
from .models import Post  # Importa o modelo Post do módulo models

# Registra o modelo Post no site de administração do Django
admin.site.register(Post)
