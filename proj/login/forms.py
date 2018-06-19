import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    usuario = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Usuario"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email"))
    senha1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Senha"))
    senha2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Senha (repetir)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['usuario'])
        except User.DoesNotExist:
            return self.cleaned_data['usuario']
        raise forms.ValidationError(_("O nome de usuário já existe. Por favor tente outro."))
 
    def clean(self):
        if 'senha1' in self.cleaned_data and 'senha2' in self.cleaned_data:
            if self.cleaned_data['senha1'] != self.cleaned_data['senha2']:
                raise forms.ValidationError(_("Os dois campos de senha não coincidem."))
        return self.cleaned_data
