import os
from pathlib import Path

# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de inicialização rápida para desenvolvimento - não adequadas para produção
# Veja https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# AVISO DE SEGURANÇA: mantenha a chave secreta usada em produção em segredo!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-7oh0at0y_btzwjr=5^l(ofhaz%mf=op1@k9p_-rsi40j$0xw%4')

# AVISO DE SEGURANÇA: não execute com debug ativado em produção!
DEBUG = False

# Defina os hosts permitidos para o projeto
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Definição das aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',  # Aplicação de administração do Django
    'django.contrib.auth',  # Aplicação de autenticação do Django
    'django.contrib.contenttypes',  # Framework de tipos de conteúdo do Django
    'django.contrib.sessions',  # Framework de sessões do Django
    'django.contrib.messages',  # Framework de mensagens do Django
    'django.contrib.staticfiles',  # Framework de arquivos estáticos do Django
    'blog',  # Aplicação de blog personalizada
]

# Definição dos middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware de segurança
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware de sessões
    'django.middleware.common.CommonMiddleware',  # Middleware comum
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware de proteção CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware de autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware de proteção contra clickjacking
]

# Configuração do URLConf raiz
ROOT_URLCONF = 'portfolio.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend de templates do Django
        'DIRS': [BASE_DIR / 'blog/templates'],  # Diretório dos templates
        'APP_DIRS': True,  # Habilita a busca de templates nos diretórios das apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Processador de contexto para debug
                'django.template.context_processors.request',  # Processador de contexto para request
                'django.contrib.auth.context_processors.auth',  # Processador de contexto para autenticação
                'django.contrib.messages.context_processors.messages',  # Processador de contexto para mensagens
            ],
        },
    },
]

# Configuração do WSGI
WSGI_APPLICATION = 'portfolio.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Backend do banco de dados SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Nome do arquivo do banco de dados
    }
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Validador de similaridade de atributos do usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validador de comprimento mínimo
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validador de senhas comuns
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validador de senhas numéricas
    },
]

# Internacionalização
LANGUAGE_CODE = 'en-us'  # Código de idioma
TIME_ZONE = 'UTC'  # Fuso horário
USE_I18N = True  # Habilita a internacionalização
USE_TZ = True  # Habilita o uso de timezones

# Arquivos estáticos (CSS, JavaScript, Imagens)
STATIC_URL = '/static/'  # URL para arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório raiz para arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Diretórios adicionais para arquivos estáticos
]

# Arquivos de mídia
MEDIA_URL = '/media/'  # URL para arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório raiz para arquivos de mídia

# Tipo de campo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração de logging para capturar erros
LOGGING = {
    'version': 1,  # Versão do esquema de logging
    'disable_existing_loggers': False,  # Não desabilita loggers existentes
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',  # Formato detalhado
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',  # Formato simples
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',  # Nível de logging
            'class': 'logging.FileHandler',  # Classe de handler de arquivo
            'filename': os.path.join(BASE_DIR, 'debug.log'),  # Nome do arquivo de log
            'formatter': 'verbose',  # Formato do log
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],  # Handlers para o logger do Django
            'level': 'DEBUG',  # Nível de logging
            'propagate': True,  # Propagação de logs
        },
    },
}
