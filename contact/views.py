from django.shortcuts import render

def inedex (request): 
    return render(
        request, 
        "contact/index.html",
        )
    