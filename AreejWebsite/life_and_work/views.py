from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from dashboard.models import Project,Memory,Interest
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def career_view(request:HttpRequest):
   projects=Project.objects.all()


   return render(request,"life_and_work/career.html",{"projects":projects})


def freespace_view(request:HttpRequest):
   memories=Memory.objects.all()
   filterdmemories=memories.filter(is_post=True)

   active_memo_id = request.GET.get('memo_id', filterdmemories.first().id)

   active_memoobject = Memory.objects.get( pk=active_memo_id)

   return render(request,"life_and_work/freespace.html",{"memories":filterdmemories,"active_memoobject":active_memoobject})

def all_interests_view(request:HttpRequest):
   interests=Interest.objects.all()
   p=Paginator(interests,3)
   page=request.GET.get('page')
   interestobj=p.get_page(page)
   return render(request,"life_and_work/all_interests.html",{"interests":interestobj})


def interest_detail_view(request:HttpRequest,interest_id):
    try:
        interest=Interest.objects.get(pk=interest_id) 
        orgnized_sources=interest.sources.split(',')  
        print(orgnized_sources) 
        return render(request,"life_and_work/interest_detail.html",{"interest":interest,"orgnized_sources":orgnized_sources})
    except Interest.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('life_and_work:all_interests_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('life_and_work:all_interests_view')
   


