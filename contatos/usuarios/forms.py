from django import forms
from usuarios.models import *
from phonenumber_field.modelfields import PhoneNumberField

# class cadastroForm(forms.Form):
#     nome= forms.CharField(
#         max_length=100,
#         label="usuario",
#         required=True,
#         widget=forms.TextInput(attrs={'placeholder': 'Ex: Silas E.', 'class': 'form-control'},
#                                )

#     )
#     email = forms.EmailField(
#         max_length=100,
#         label="E-mail",
#         required=True,
#         widget=forms.EmailInput(
#             attrs={'placeholder': 'Ex: usuario@mysite.com', 'class': 'form-control'}),

#     )
#     Telefone = forms.CharField(
#         max_length=100,
#         label="Telefone",
#         required=True,
#     )

    
#     imagem = forms.FileInput(
#         max_length=100,
#         label="Senha",
#         required=True,
#         widget=forms.FileInput(
#             attrs={'class': 'form-control'}),

#     )



class cadastroForm(forms.ModelForm):
    class Meta:
        model = usuario
        exclude = ['data_fotografia',]
        labels = {
            'nome': 'Usuário',
        }       
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','placeholder':"Ex. Silas Eduardo"}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':"Ex. usuario@meuemail.com"}),
            'Telefone': forms.TextInput(attrs={'class': 'form-control','placeholder':"Ex. +5531997793112"}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }
