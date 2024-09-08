from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Modelo Author - Relacionamento um-para-um com o modelo User do Django
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Biografia", help_text="Digite uma breve biografia do autor")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.user.username


# Modelo Post - Relacionamento muitos-para-um com o modelo Author
class Post(models.Model):
    # Definindo as opções de status do post
    STATUS_CHOICES = (
        (0, 'Rascunho'),
        (1, 'Publicado'),
    )

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug", blank=True)  # Adicionado blank=True
    content = models.TextField(verbose_name="Conteúdo")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Autor")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")

    class Meta:
        ordering = ['-created_on']  # Ordena posts mais recentes primeiro
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    # Sobrescrever o método save para gerar automaticamente o slug
    def save(self, *args, **kwargs):
        if not self.slug:  # Gerar slug apenas se não estiver preenchido
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
