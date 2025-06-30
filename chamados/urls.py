from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_chamados, name='lista_chamados'),
    path('login/', views.fazer_login, name='login'),
    path('perfil/', views.perfil_informacoes, name='perfil' ),
    path('chamado/<int:chamado_id>/favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('cadastra/', views.cadastra_usuario, name='cadastra'),
    path('novo/', views.criar_chamado, name='criar_chamado'),
    path('editar/<int:id>/', views.editar_chamado, name='editar_chamado'),
    path('deletar/<int:id>/', views.deletar_chamado, name='deletar_chamado'),
    path('chamado/<int:chamado_id>/status/', views.atualizar_status, name='atualizar_status'),
    path('detalhes/<int:id>/', views.detalhes_chamado, name='detalhes_chamado'),
]
