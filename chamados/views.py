from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Chamado, User
from .forms import ChamadoForm, LoginForm, EditarUsuarioForm, RegisterUser, AtendimentoForm
from chamados.utils import filtrar_chamados


def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.autenticar(email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('lista_chamados')
            else:
                messages.error(request, 'Usuario ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def cadastra_usuario(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('lista_chamados')
    else:
        form = RegisterUser()
    return render(request, 'cadastra.html', {'form': form})

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.filter(usuario=request.user)
    chamados = filtrar_chamados(chamados, request.GET)


    total_chamados = Chamado.objects.count()
    em_andamento = Chamado.objects.filter(status='em_andamento').count()
    a_fazer = Chamado.objects.filter(status='aberto').count()
    resolvidos = Chamado.objects.filter(status='resolvido').count()

    prioridades = ['Baixa', 'Média', 'Alta', 'Urgente']

    for chamado in chamados:
        chamado.form = AtendimentoForm(instance=chamado) 
        
    context = {
        'total_chamados': total_chamados,
        'em_andamento': em_andamento,
        'a_fazer': a_fazer,
        'resolvidos': resolvidos,
        'prioridades':prioridades, 
        'chamados': chamados,
    }
    return render(request, 'chamados/lista.html', context) 

def toggle_favorito(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)
    chamado.favorito = not chamado.favorito
    chamado.save()
    return redirect('lista_chamados')

@login_required
def perfil_informacoes(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil') 
    else:
        form = EditarUsuarioForm(instance=request.user)

    return render(request, 'chamados/perfil.html', {'form': form})

@login_required
def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.usuario = request.user
            chamado.save()
            return redirect('lista_chamados')
    else:
        form = ChamadoForm()
    return render(request, 'chamados/form.html', {'form': form})

@login_required
def editar_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('lista_chamados')
    else:
        form = ChamadoForm(instance=chamado)
    return render(request, 'chamados/form.html', {'form': form})

@login_required
def deletar_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, usuario=request.user)
    if request.method == 'POST':
        chamado.delete()
        return redirect('lista_chamados')
    return render(request, 'chamados/confirmar_exclusao.html', {'chamado': chamado})

@login_required
def atender_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id)

    if chamado.status == 'resolvido':
        return render(request, 'chamados/erro.html', {
            'mensagem': 'Este chamado já foi resolvido e não pode ser alterado.'
        })

    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=chamado)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.atendente = request.user
            atendimento.save()
            return redirect('lista_chamados')
    else:
        form = AtendimentoForm(instance=chamado)

    return render(request, 'chamados/atender.html', {'form': form, 'chamado': chamado})

@login_required
def detalhes_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id)
    return render(request, 'chamados/detalhes.html', {'chamado': chamado})

@login_required
def atualizar_status(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
    return redirect('lista_chamados')
