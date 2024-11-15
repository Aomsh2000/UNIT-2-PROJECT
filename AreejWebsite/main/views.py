from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from main.models import Contact
from django.contrib import messages
from .forms import ContactForm
from dashboard.models import Project,Memory,Interest

# Create your views here.

def home_view(request:HttpRequest):
    projects=Project.objects.all()[0:3]

    return render(request,"main/home.html",{"projects":projects})


def home_view_filter(request:HttpRequest,filter_choice):
    
    if filter_choice == 'projects':
        projects=Project.objects.all()[0:3]
        return render(request,"main/home.html",{"projects":projects,"filter_choice":filter_choice})
    elif filter_choice == 'memories':
        memories=Memory.objects.all()
        filterdmemories=memories.filter(is_post=True)[0:3]

        return render(request,"main/home.html",{"memories":filterdmemories,"filter_choice":filter_choice})
    elif filter_choice == 'interests':
        interests=Interest.objects.all()[0:3]
        return render(request,"main/home.html",{"interests":interests,"filter_choice":filter_choice})
        
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





