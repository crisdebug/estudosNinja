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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LogIn.as_view() , name='login'),
    path('cadastro/', views.SignUp.as_view(), name='cadastro'),
    path('criar-turma/', views.criar_turma, name='criar-turma'),
    path('logout/', auth_views.logout, {'next_page':'/'}, name='logout'),
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('e/<str:codigo>/', views.entrar_turma, name='entrar-turma'),
    path('turmas/', views.ver_turmas, name='ver-turmas'),
    path('v/<str:codigo>/', views.ver_turma, name='ver-turma'),
    path('v/<str:codigo_turma>/criar', views.criar_atividade, name='criar-atividade'),
    path('v/<str:codigo_turma>/a/<int:ak>', views.ver_atividade, name='ver-atividade'),
    path('comments/', include('django_comments.urls'))
]
