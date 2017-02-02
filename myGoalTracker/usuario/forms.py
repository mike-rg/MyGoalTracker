from django import forms
from django.contrib.auth.models import User

from usuario.models import Usuario


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = "__all__"
        fields = ('first_name', 'last_name', 'email', )


class UsuarioForm(forms.ModelForm):

    class Meta:
         model = Usuario
         exclude = ['usuario']
         fields = ('foto', )
