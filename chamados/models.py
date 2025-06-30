from django.db import models
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    NIVEL = [
        ('Usuário', 'Usuário'),
        ('Atendente', 'Atendente'),
        ('Administrador', 'Administrador'),
    ]

    username = None
    email = models.EmailField(('email address'), unique=True)
    nivelUser = models.CharField(max_length=15, choices=NIVEL, default='Usuário')
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    codigo_cadastro = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['nome_completo'] 

    @classmethod
    def autenticar(cls, email, password):
        from django.contrib.auth import authenticate
        return authenticate(email=email, password=password)
    
    def __str__(self):
        return self.nome_completo or self.email


class Chamado(models.Model):
    PRIORIDADES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
        ('Urgente', 'Urgente'),
    ]

    STATUS = [
        ('aberto', '⏳ Aberto'),
        ('em_andamento', '🛠️ Em Andamento'),
        ('resolvido', '🎉 Resolvido'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    status = models.CharField(max_length=15, choices=STATUS, default='aberto')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamados')
    data_criacao = models.DateTimeField(auto_now_add=True)
    favorito = models.BooleanField(default=False)

    resposta = models.TextField(blank=True, null=True)
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chamados')
    atendente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='atendimentos')

    def __str__(self):
        return self.titulo
