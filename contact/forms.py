
from contact.models import Contact
from django import forms #type: ignore
from . import models
from django.core.exceptions import ValidationError #type: ignore


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name","last_name", "phone",)

        widgets = {
            "first_name" : forms.TextInput(
                attrs= {
                    "class":"classe - a",
                    "placeholder":" Escreva aqui"
                }
            )
        }

    def clean(self):
        
        return super().clean()

