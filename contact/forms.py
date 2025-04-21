from . import models
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs= {
    #             'class': 'classe-a classe-b', # atributos do widgets
    #             'placeholder': "Escreva aqui",
    #         }
    #     ),
    #     label="Primeiro Nome",
    #     help_text="Texto de ajuda para o usuario",
    # )

    # Este campo nao esta ligado ao model, poderia ser um re captcha?
    # campo_qualquer = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs= {
    #             'class': 'classe-a classe-b', # atributos do widgets
    #             'placeholder': "Escreva aqui",
    #         }
    #     ),
    #     label="Qualquer",
    #     help_text="Texto de ajuda para o usuario",
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({ # Atualiza o widget
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Escreva aqui',
        # })
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
        )
        # widgets = { # Cria um novo widget
        #     'first_name': forms.TextInput( # mesmo do field
        #         attrs= {
        #             'class': 'classe-a classe-b', # atributos do widgets
        #             'placeholder': "Escreva aqui",
        #         }
        #     ),
        # }
    
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