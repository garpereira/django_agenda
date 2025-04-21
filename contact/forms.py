from . import models
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
        )
    
    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        
        return super().clean()