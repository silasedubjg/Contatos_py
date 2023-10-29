from django.contrib import admin
from usuarios.models import usuario

class usuarioadmin(admin.ModelAdmin):
    list_display = ("nome", "email", "Telefone","imagem","data_fotografia")
    list_display_links = ("nome", "email", "Telefone","imagem","data_fotografia")
# Register your models here.
admin.site.register(usuario, usuarioadmin)
