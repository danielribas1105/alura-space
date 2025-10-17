from django.db import models

class Usuario(models.Model):
   
   def __str__(self):
      return self.nome