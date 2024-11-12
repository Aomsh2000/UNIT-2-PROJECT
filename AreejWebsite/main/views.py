from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from main.models import Contact
from django.contrib import messages
from .forms import ContactForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def home_view(request:HttpRequest):

    return render(request,"main/home.html")


def contact_view(request:HttpRequest):
    if request.method=="POST":
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
              contact_form.save()
              messages.success(request, 'The massege has been send successfully!')
              return redirect("main:contact_view")
        else:
            print("form is not valid")
            print(contact_form.errors)   

    return render(request,"main/contact.html") 


def messages_view(request:HttpRequest):
    pass



