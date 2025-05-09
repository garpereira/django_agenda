from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q # OR
from django.core.paginator import Paginator


def index(request):
    page_obj = False

    if request.user.pk: 
        contacts = Contact.objects.filter(show=True).filter(owner=request.user).order_by("-id")
        paginator = Paginator(contacts, 10) # Mostar 10 contatos por pagina
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    return render(
        request,
        "contact/index.html",
        context,
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    
    site_title = f"{single_contact.first_name} {single_contact.last_name} - "

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        "contact/contact.html",
        context,
    )

def search(request):
    search_value =  request.GET.get("q", "").strip()
    
    if search_value == "":
        return redirect("contact:index")

    # LookUps
    contacts = Contact.objects\
        .filter(owner=request.user)\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        ).order_by("-id")
    paginator = Paginator(contacts, 10) # Mostar 10 contatos por pagina
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    context = {
        "page_obj": page_obj,
        "site_title": "Search - ",
    }

    return render(
        request,
        "contact/index.html",
        context,
    )