
from contact.models import Contact
from django import forms 
from . import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError #type: ignore
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation 

class ContactForms(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*"
            }
        ),
        required=False
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

class RegisterForm(UserCreationForm):

    


    first_name = forms.CharField(
        required=True,
        min_length= 3,
    )
    last_name = forms.CharField(
        required=True,
        min_length= 3,
    )
    email = forms.CharField()
    class Meta():
        model = User
        fields = (
            "first_name","last_name", "email","username","password1","password2"
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            self.add_error(
                "email", ValidationError ("email ja existe", code= "invalid")

            )
        return email
            
class RegisterUpdateForm (forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="required",
        error_messages={
            "min_length":"please, add more than 2 letters"
        }
    )
    last_name = forms.CharField(
    min_length=2,
    max_length=30,
    required=True,
    help_text="required",
   
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete":"new_password"}),
        help_text= password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete":"new_password"}),
        help_text= "use the same password as before",
        required=False
                    )
    
    
    class Meta:
        model = User
        fields = (
            "first_name","last_name","email",
            "username",
        )

    def save(self, commit= True): 
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get("password1")

        if password:
            user.set_password(password)
        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            self.add_error(
                "password2",
                ValidationError("senhas não batem")
            )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email = email).exists():
                self.add_error(
                    "email", ValidationError ("email ja existe", code= "invalid")

                )
        return email
    
    def clean_password1(self):
        password1 =  self.cleaned_data.get("password1")

        if password1:
            try:
                password_validation.validate_password(password1) 
            except ValidationError as errors:
                self.add_error("password1", ValidationError(errors))

        return password1
    