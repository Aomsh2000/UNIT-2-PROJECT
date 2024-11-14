from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def career_view(request:HttpRequest):

   return render(request,"life_and_work/career.html")


def freespace_view(request:HttpRequest):

   return render(request,"life_and_work/freespace.html")


def interest_detail_view(request:HttpRequest,interest_id):

   return render(request,"life_and_work/interest_detail.html")


def memo_detail_view(request:HttpRequest,memo_id):

   return render(request,"life_and_work/memo_detail.html")


def project_detail_view(request:HttpRequest,project_id):

   return render(request,"life_and_work/project_detail.html")