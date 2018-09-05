from django.db import models
from django_comments.abstracts import BaseCommentAbstractModel
from django.contrib.auth.models import User

# Create your models here.
class Comentario(BaseCommentAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()