from django.forms import ModelForm
from .models import *
from django import forms


class FormVenda(ModelForm):


    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormVenda, self).__init__(*args, **kwargs)
    
    def nome(self):
        return "venda"

    class Meta():
        model = Venda
        fields = '__all__'
        exclude = ['create_at', 'update_at']

class FormDispositivos(ModelForm):


    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormDispositivos, self).__init__(*args, **kwargs)

    class Meta():
        model = Dispositivos
        fields = '__all__'
        exclude = ['create_at', 'update_at']