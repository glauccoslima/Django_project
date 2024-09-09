from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post

# View para a página inicial (index.html), que lista os posts
class PostView(View):
    @staticmethod  # Converte o método em um método estático, pois não usa a instância da classe
    def get(request):
        # Obtém todos os posts do banco de dados
        post_list = Post.objects.all()
        # Renderiza o template 'index.html' passando a lista de posts
        return render(request, 'index.html', {'post_list': post_list})


# View para exibir o detalhe de um post específico (post_detail.html)
class PostDetailView(View):
    @staticmethod  # Converte o método em um método estático, pois não usa a instância da classe
    def get(request, slug):
        # Obtém o post correspondente ao slug ou retorna 404 se não encontrado
        post = get_object_or_404(Post, slug=slug)
        # Renderiza o template 'post_detail.html' com o post especificado
        return render(request, 'post_detail.html', {'post': post})
