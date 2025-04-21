from . import models
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )

    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        msg = ValidationError(
            'Primeiro nome não pode ser igual ao segundo',
            code='invalid'
        )
        if first_name == last_name:
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro do clean',
        #         code='invalid'
        #     )
        # )
        return super().clean()

    # Da para tratar o que é recebido no post do forms antes de fato ir para o banco
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            # raise ValidationError( # raise faz o codigo parar neste ponto
            #     'Não digite ABC neste campo',
            #     code='invalid',
            # )
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro do clean_first_name',
                    code='invalid',
                )
            )  
        return first_name