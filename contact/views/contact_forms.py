from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
        }
        
        if form.is_valid():
            # contact = form.save(commit=False) # Segura o formulario aqui para fazer alterações antes de salvar
            contact = form.save()
            
            return redirect('contact:create')

        return render(
            request,
            "contact/create.html",
            context,
        )

        
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        "contact/create.html",
        context,
    )