"""
estudosNinja URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from atividades import views
<<<<<<< HEAD
from comments import views as comment_views
=======
>>>>>>> 5c5504ede013a241303215239b275d7941ccb209

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginAluno.as_view() , name='login'),
    path('cadastro/', views.SignUp.as_view(), name='cadastro'),
    path('criar-turma/', views.CriarTurmaView.as_view(), name='criar-turma'),
<<<<<<< HEAD
    path('logout/', auth_views.LogoutView.as_view(), {'next_page':'/'}, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
=======
    path('logout/', auth_views.logout, {'next_page':'/'}, name='logout'),
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
>>>>>>> 5c5504ede013a241303215239b275d7941ccb209
    path('e/<str:codigo>/', views.adicionar_aluno, name='adicionar-aluno'),
    path('entrar/', views.EntrarTurmaView.as_view(), name='entrar-turma'),
    path('turmas/', views.TurmasView.as_view(), name='ver-turmas'),
    path('v/<str:codigo>/', views.VerTurmaView.as_view(), name='ver-turma'),
<<<<<<< HEAD
    path('v/<str:codigo_turma>/criar/', views.CriarAtividadeView.as_view(), name='criar-atividade'),
    path('v/<str:codigo_turma>/a/<int:ak>', views.VerAtividadeView.as_view(), name='ver-atividade'),
    path('atividades/', views.VerAtividadesView.as_view(), name='atividades'),
    path('sair/', views.sair, name='sair'),
    path('comments/', include('django_comments.urls')),
    path('postar/', comment_views.post_comment, name='postar-comentario')

=======
    path('v/<str:codigo_turma>/criar', views.CriarAtividadeView.as_view(), name='criar-atividade'),
    path('v/<str:codigo_turma>/a/<int:ak>', views.VerAtividadeView.as_view(), name='ver-atividade'),
    path('sair/', views.sair, name='sair'),
    path('comments/', include('django_comments.urls'))
>>>>>>> 5c5504ede013a241303215239b275d7941ccb209
]
