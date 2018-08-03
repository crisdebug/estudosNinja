from django.contrib import admin

from .models import Aluno_em_Turma, Turma
# Register your models here.
admin.site.register(Turma)
admin.site.register(Aluno_em_Turma)