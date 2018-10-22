from django.db import models
from django_comments.abstracts import BaseCommentAbstractModel
<<<<<<< HEAD

class ComentarioModel(BaseCommentAbstractModel):
    comment = models.CharField(max_length=300)
=======
from django.contrib.auth.models import User

# Create your models here.
class Comentario(BaseCommentAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
>>>>>>> 5c5504ede013a241303215239b275d7941ccb209
