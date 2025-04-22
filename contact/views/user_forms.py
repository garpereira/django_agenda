from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm

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
            return redirect('contact:register')

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