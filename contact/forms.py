from . import models
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False,
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
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nome',
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        label='Sobrenome',
        required=True,
        min_length=3,
    )

    email = forms.EmailField(
        required=True,
    )
    
    class Meta:
        model = User
        fields = ( 
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # if '@algumacoisa' not in email:
        #     self.add_error(
        #         'email',
        #         ValidationError(
        #             "Insira um email válido",
        #             code='invalid',
        #         )
        #     )

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    "Um cadastro com esse email já existe.",
                    code='invalid'),
            )

        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=30,
        required=True,
        help_text='Campo Obrigatório.',
        error_messages={
            'min_length': f'O nome precisa ter três letras ou mais',
        }
    )

    last_name = forms.CharField(
        min_length=3,
        max_length=30,
        required=True,
        help_text='Campo Obrigatório.',
    )

    email = forms.EmailField(
        disabled=False,
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
            }
        ),
        help_text=password_validation.password_validators_help_texts(),
        required=False,
    )
    password2 = forms.CharField(
        label="Confirmação de senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
            }
        ),
        help_text="Insira a mesma senha definida no campo anterior.",
        required=False,
    )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError(
                        'Senhas devem ser iguais.',
                        code='invalid',
                    ),
                )
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        "Um cadastro com esse email já existe.",
                        code='invalid',
                    ),
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(
                        errors,
                        code='invalid',
                    ),
                )
        
        return password1
    

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )