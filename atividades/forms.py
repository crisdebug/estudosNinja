from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome'}),max_length=30, required=True, help_text='*')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'}),max_length=30, required=True, help_text='*')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}),max_length=254, help_text='Informe um Email válido', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Senha'}), required=True, min_length=8, max_length=16)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repita a Senha'}), required=True, min_length=8, max_length=16)



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')