from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    user = RegisterForm()
    # messages.info(request, 'um texto qualquer')
    # messages.success(request, 'um texto qualquer')
    # messages.warning(request, 'um texto qualquer')
    # messages.error(request, 'um texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('contact:login')

        return render(
        request,
        "contact/register.html",
        {
        "form": form
        }
    )

    return render(
        request,
        "contact/register.html",
        {
        "form": user
        }
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Acesso realizado com sucesso!')
            return redirect('contact:index')
        # da para criar o proprio sistema de erros ou utilizar o do django com o non_field_errors
        else:
            messages.error(request, 'Login inválido, usuário e/ou senha estão incorretos.')
            
    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)

    return redirect('contact:login')


@login_required(login_url='contact:login')
def update_view(request):

    if request.method != 'POST':
        form = RegisterUpdateForm(instance=request.user)
        return render(
            request,
            'contact/update.html',
            {
                'form': form,
            }
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/update.html',
            {
                'form': form,
            }
        )
    
    form.save()
    return redirect('contact:update')