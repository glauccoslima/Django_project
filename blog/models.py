from django.db import models
from django.contrib.auth.models import User

# Modelo Author - Relacionamento 1:1 com User
class Author(models.Model):
    # Campo de relacionamento um-para-um com o modelo User do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Campo de texto para a biografia do autor
    bio = models.TextField()

    # Método para retornar o nome de usuário do autor como string
    def __str__(self):
        return self.user.username


# Modelo Post - Relacionamento 1:N com Author
class Post(models.Model):
    # Definição das opções de status do post
    STATUS_CHOICES = (
        (0, 'Draft'),  # Rascunho
        (1, 'Published')  # Publicado
    )

    # Campo de texto para o título do post, com limite de 200 caracteres
    title = models.CharField(max_length=200)
    # Campo de texto para o conteúdo do post
    content = models.TextField()
    # Campo de relacionamento muitos-para-um com o modelo Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Campo de data e hora para a criação do post, preenchido automaticamente
    created_on = models.DateTimeField(auto_now_add=True)
    # Campo inteiro para o status do post, com opções definidas em STATUS_CHOICES e valor padrão 0 (Rascunho)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    # Método para retornar o título do post como string
    def __str__(self):
        return self.title
