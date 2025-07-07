
from contact.models import Contact
from django import forms 
from . import models
from django.core.exceptions import ValidationError #type: ignore


class ContactForms(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*"
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            "first_name","last_name", "phone",
            "email","description", "Category",
            "picture",
            )


    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if first_name == last_name:
            msg = ValidationError(" nome e sobrenome não podem ser iguais", code= "invalid")

            self.add_error("first_name", msg)
            self.add_error("last_name", msg)
        
        return super().clean()
    
    def clean_first_name(self):

        first_name = self.cleaned_data.get("first_name")

        if first_name == "ABC":
            self.add_error\
            (
            "first_name", 
            ValidationError 
                (
                "veio do add_error",
                code= "invalid"
                )
            )
        return first_name

