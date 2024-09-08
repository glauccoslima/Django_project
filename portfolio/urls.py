from django.contrib import admin
from django.urls import path
from blog.views import PostView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin habilitado
    path('home/', PostView.as_view(), name='home-view'),
]

# Servir arquivos estáticos e de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
