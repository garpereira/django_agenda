from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q # OR
from django.core.paginator import Paginator
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
        )


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
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