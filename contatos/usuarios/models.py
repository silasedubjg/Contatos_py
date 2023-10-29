from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.

class usuario(models.Model, PhoneNumberField):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=200,null=True,blank=True)
    Telefone = PhoneNumberField(null=False, blank=False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_fotografia = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"usuario [nome={self.nome}]"