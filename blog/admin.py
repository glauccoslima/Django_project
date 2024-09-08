from django.contrib import admin
from .models import Author, Post

# Configuração para o modelo Author no Django Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ['user__username', 'bio']
    ordering = ['user__username']  # Ordena os autores alfabeticamente pelo nome de usuário
    list_per_page = 10  # Limita a exibição para 10 autores por página


# Configuração para o modelo Post no Django Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {"slug": ("title",)}  # Preenche automaticamente o campo slug com base no título
    date_hierarchy = 'created_on'  # Adiciona um filtro hierárquico por data
    ordering = ['status', 'created_on']  # Ordena primeiro pelo status, depois pela data
    list_per_page = 10  # Limita a exibição para 10 posts por página

    # Torna 'created_on' somente leitura, já que é preenchido automaticamente
    readonly_fields = ('created_on',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content')
        }),
        ('Opções Avançadas', {
            'classes': ('collapse',),  # Permite que a seção seja colapsada
            'fields': ('status', 'created_on'),  # 'created_on' é apenas leitura
        }),
    )
