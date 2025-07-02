#type: ignore

from typing import Any
from django.shortcuts import render,get_object_or_404, redirect
from contact.models import Contact
from django.core.paginator import Paginator 
from django import forms
from contact.forms import ContactForms


def create (request):
    if request.method == "POST":
        context = {
                "form" : ContactForms(request.POST)
        }

        return render(
            request, 
            "contact/create.html",
            context
            )

    context = {
            "form" : ContactForms()
           }

    return render(
        request, 
        "contact/create.html",
        context
        )

 