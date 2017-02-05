from django import forms

from meta.models import Usuario, Meta


class MetaForm(forms.ModelForm):

    class Meta:
        model = Meta
        exclude = "__all__"
        fields = ('titulo', 'descripcion', 'fecha_comienzo', )
