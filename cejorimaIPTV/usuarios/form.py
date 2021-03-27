from .models import *
from django import forms
from django.forms import ModelForm


class FormCliente(ModelForm):


    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormCliente, self).__init__(*args, **kwargs)

    class Meta():
        model = Cliente
        fields = '__all__'
        exclude = ['create_at', 'update_at', 'adm']
        widgets = {
            'senha': forms.PasswordInput(),
        }


class FormLogin(ModelForm):


    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormLogin, self).__init__(*args, **kwargs)

    class Meta():
        model = Usuario
        fields = '__all__'
        exclude = ['nome', 'telefone', 'cpf', 'create_at', 'update_at']
        widgets = {
            'senha': forms.PasswordInput(),
        }