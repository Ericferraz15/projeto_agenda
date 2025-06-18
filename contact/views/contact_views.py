#type: ignore

from django.shortcuts import render
from contact.models import Contact


def inedex (request): 
    Contacts = Contact.objects.all()
    context = {
        "contacts": Contacts,
    }

    return render(
        request, 
        "contact/index.html",
        context
        )
 