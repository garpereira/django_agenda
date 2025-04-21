from . import models
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class': 'classe-a classe-b', # atributos do widgets
                'placeholder': "Escreva aqui",
            }
        ),
        label="Primeiro Nome",
        help_text="Texto de ajuda para o usuario",
    )

    # Este campo nao esta ligado ao model, poderia ser um re captcha?
    campo_qualquer = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class': 'classe-a classe-b', # atributos do widgets
                'placeholder': "Escreva aqui",
            }
        ),
        label="Qualquer",
        help_text="Texto de ajuda para o usuario",
    )

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

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        
        return super().clean()