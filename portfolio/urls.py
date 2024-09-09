from django.contrib import admin
from django.urls import path
from blog.views import PostView, PostDetailView  # Importando a view para detalhes do post
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect  # Importando redirect

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin habilitado
    path('', lambda request: redirect('home-view')),  # Redireciona a raiz para /home/
    path('home/', PostView.as_view(), name='home-view'),  # Página inicial (lista de posts)
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),  # Página de detalhes do post
]

# Servir arquivos estáticos e de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
