from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Chamado, User

class RegisterUser(UserCreationForm):
     class Meta:
        model = User
        username = None
        email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
        nome_completo = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
        nivelUser = forms.ChoiceField(choices=User.NIVEL, initial='usuario', widget=forms.Select(attrs={'class': 'form-control'}))
        telefone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        foto_perfil = forms.ImageField(required=False)
        codigo_cadastro = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        fields = [
            'nome_completo',
            'email',
            'nivelUser',
            'telefone',
            'foto_perfil',
            'codigo_cadastro',
            'password1',
            'password2'
        ]

        password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
        )
        password2 = forms.CharField(
            label="Confirme sua senha",
            widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
        )

        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Primeiro Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'codigo_cadastro': forms.TextInput(attrs={'placeholder': 'Código de funcionário'}),
        }    

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nome_completo',
            'email',
            'nivelUser',
            'telefone',
            'foto_perfil',
            'codigo_cadastro',
        ]

class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo','descricao','prioridade']

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite aqui o titulo:'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Digite aqui a descrição:'}),
        }

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    