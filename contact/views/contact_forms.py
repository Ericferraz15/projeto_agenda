#type: ignore

from typing import Any
from django.shortcuts import render,get_object_or_404, redirect
from contact.models import Contact
from django.core.paginator import Paginator 
from django import forms
from contact.forms import ContactForms, Contact
from django.urls import reverse


def create (request):
    form_action  = reverse("contact:create")
    
    if request.method == "POST":
        form =  ContactForms(request.POST, request.FILES)
        context = {
                "form" : form,
                "form_action": form_action
        }

        if form.is_valid(): 
            contact = form.save()
            return redirect('contact:update', contact.pk)

        return render(
            request, 
            "contact/create.html",
            context
            )


    context = {
                "form" : ContactForms(),
                "form_action": form_action,
        }
    return render(
        request, 
        "contact/create.html",
        context
        )


def update (request,contact_id):
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
        )
    form_action  = reverse("contact:update",args=(contact_id,))
    
    if request.method == "POST":
        form =  ContactForms(request.POST,request.FILES,instance=contact,)
        context = {
                "form" : form,
                "form_action": form_action
        }

        if form.is_valid():
            form.save()
            return redirect("contact:update", contact_id = contact.pk)

        return render(
            request, 
            "contact/create.html",
            context
            )


    context = {
                "form" : ContactForms(instance=contact),
                "form_action": form_action,
        }
    return render(
        request, 
        "contact/create.html",
        context
        )

def delete (request,contact_id):
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
        )
    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index")
    
    return render (
        request,
        "contact/contact.html",
        {
            "contact" : contact,
            "confirmation" : confirmation
        }
    )