from django.shortcuts import render
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def Register(request):
    form = RegisterForm()

    if request.method == "POST":
     form = RegisterForm(request.POST)

     if form.is_valid():
        form.save()
        messages.success(request, "usuario registrado com sucesso")
        return redirect("contact:login")
    
    return render(
        request,
        "contact/register.html",
        {
            'form': form
        }
    )


def login_view(request):
    form = AuthenticationForm(request)    

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
           user = form.get_user()
           auth.login(request, user)
           messages.success(request,"sucesso ao logar")
           return redirect("contact:index")
        messages.error(request, "login invalido")


    return render(
        request,
        "contact/login.html",
        {
            'form': form
        }
    )

def logout_view(request):
   auth.logout(request)
   return redirect("contact:login")


@login_required(login_url="contact:login")
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
       
    if request.method != "POST": 
        return render(
            request,
            "contact/update_user.html",
            {
                'form': form
            }
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
       
    if not form.is_valid():
        return render(
        request,
        "contact/update_user.html",
        {
            'form': form
        }
        )
    form.save() 
    return redirect("contact:user_update")