
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth import login, authenticate
from django.views.generic import FormView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 

from atividades.forms import SignUpForm, LogInForm

# Create your views here.



class SignUp(FormView):
    template_name = 'atividades/cadastro.html'
    form_class = SignUpForm
    success_url = reverse_lazy('logou')

    def form_valid(self, form):
        aluno = form.save(commit = False)
        aluno.save()
        messages.success(self.request, "Aluno cadastrado com sucesso")
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.error(self.request, "Por favor, preencha corretamente os campos")
        return self.render_to_response(self.get_context_data(form = form))


class LogIn(FormView):
    template_name = 'atividades/login.html'
    form_class = LogInForm
    success_url = reverse_lazy('logou')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LogIn, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogouView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'atividades/logou.html'