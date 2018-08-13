import string
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import login, authenticate, views as auth_views
from django.views.generic import FormView, TemplateView, ListView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required

from atividades.forms import SignUpForm, LogInForm, CriarTurmaForm, CriarAtividadeForm
from atividades.models import Aluno_em_Turma, Turma, Atividade

# Create your views here.



class SignUp(FormView):
    template_name = 'atividades/cadastro.html'
    form_class = SignUpForm
    success_url = reverse_lazy('criar-turma')

    def form_valid(self, form):
        aluno = form.save(commit = False)
        aluno.email = form.cleaned_data['username']
        aluno.save()
        messages.success(self.request, "Aluno cadastrado com sucesso")
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.error(self.request, "Por favor, preencha corretamente os campos")
        return self.render_to_response(self.get_context_data(form = form))


class LogIn(FormView):
    template_name = 'atividades/login.html'
    form_class = LogInForm
    success_url = reverse_lazy('ver-turmas')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LogIn, self).form_valid(form)
        else:
            return self.form_invalid(form)

def criar_turma(request):
    if request.method == 'POST':
        form = CriarTurmaForm(request.POST)
        if form.is_valid():
            codigo = gerar_codigo()
            return HttpResponseRedirect('entrar-turma', codigo=codigo)
    else:
        form = CriarTurmaForm()
    return render(request, 'atividades/criar_turma.html', {'form':form})

@login_required
def entrar_turma(request, codigo):
    if request.user.is_authenticated():
        if testar_codigo(codigo):
            a = Aluno_em_Turma(id_usuario=request.user.get_id(), codigo=codigo)
            a.save()
            return HttpResponseRedirect('v/%s' % codigo)
    return render(request, '')

@login_required
def ver_turma(request, codigo):
    turma = Turma.objects.get(codigo=codigo)
    atividades = Atividade.objects.filter(turma=turma)
    return render(request, 'atividades/ver_turma.html', {'atividades':atividades, 'turma':turma})

@login_required
def ver_turmas(request):
    turmas = Aluno_em_Turma.objects.filter(id_usuario=request.user)
    return render(request, 'atividades/turmas.html', {'turmas':turmas})

@login_required
def criar_atividade(request, codigo_turma):
    if request.method == 'POST':
        atividade = CriarAtividadeForm(request.POST).save(commit=False)
        atividade.turma = Turma.objects.get(codigo=codigo)
        atividade.criador = request.user
        atividade.save()
        return HttpResponseRedirect('ver-atividade', codigo=codigo, ak=atividade.id)

    else:
        form = CriarAtividadeForm()
    return render(request, 'atividade/criar_atividade.html', {'form':form})

@login_required
def ver_atividade(request, codigo_turma, ak):
    atividade = Atividade.objects.get(id=ak, turma=Turma.objects.get(codigo=codigo_turma))
    return render(request, 'atividades/atividade.html', {'atividade':atividade})

def testar_codigo(codigo):
    try:
        Turma.objects.get(codigo=codigo)
        return True
    except:
        return False

def gerar_codigo(size=5, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    codigo = ''.join(random.choice(chars) for x in range(size))
    if testar_codigo(codigo):
        codigo = gerar_codigo()
    return codigo

