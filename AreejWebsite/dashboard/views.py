from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.contrib import messages
from django.core.paginator import Paginator
from main.models import Contact
from .forms import InterestForm,ProjectForm,MemoryForm
from .models import Interest,Project,Memory
# Create your views here.

def dashboard_view(request:HttpRequest):
   return render(request,"dashboard/dashboard.html")

# Masseges viwes
def messages_view(request:HttpRequest):
   masseges=Contact.objects.all()
    
   if "search" in request.GET and len(request.GET["search"])>=1:
        masseges = Contact.objects.filter(name__icontains=request.GET["search"])

   if "order_by" in request.GET and request.GET["order_by"] == "created_at":
            masseges=masseges.order_by("-created_at")
    
   p=Paginator(masseges,4)
   page=request.GET.get('page')
   massegeobj=p.get_page(page)

   return render(request,"dashboard/messages.html",{"masseges":massegeobj})

def read_message_view(request, message_id):
    try: 
        message=Contact.objects.get(pk=message_id)
        
        return render(request,"dashboard/read_message.html",{"message":message})
    except Contact.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:messages_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('dashboard:messages_view')



def delete_message_view(request:HttpRequest,message_id):
  try:
        message=Contact.objects.get(pk=message_id)
        message.delete()
        return redirect('dashboard:messages_view')
  except Contact.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:messages_view')
  except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('dashboard:messages_view')
  

# Intrests views

def interests_view(request:HttpRequest):
   interests=Interest.objects.all()
    
   if "search" in request.GET and len(request.GET["search"])>=1:
        interests = Interest.objects.filter(subject__icontains=request.GET["search"])

   if "order_by" in request.GET and request.GET["order_by"] == "created_at":
            interests=interests.order_by("-created_at")
    
   p=Paginator(interests,4)
   page=request.GET.get('page')
   interestobj=p.get_page(page)

   return render(request,"dashboard/interests.html",{'interests':interestobj})


def add_interest_view(request:HttpRequest):
      
      if request.method=="POST":
        interest_form=InterestForm(request.POST,request.FILES)
        if interest_form.is_valid():
              interest_form.save()
              messages.success(request, 'The interest has been added successfully!')
              return redirect("dashboard:add_interest_view")
        else:
            print("form is not valid")
            print(interest_form.errors)   

      return render(request,"dashboard/add_interest.html")



def delete_interest_view(request:HttpRequest,interest_id):
  try:
        interest=Interest.objects.get(pk=interest_id)
        interest.delete()
        return redirect('dashboard:interests_view')
  except Interest.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:interests_view')
  except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('dashboard:interests_view')
  
def update_interest_view(request:HttpRequest,interest_id):
    try:  
        interest=Interest.objects.get(pk=interest_id)
        if request.method=="POST":
            interest_form=InterestForm(request.POST,request.FILES,instance=interest)
            if interest_form.is_valid():
                interest_form.save()
                messages.success(request, 'The interest has been updated successfully!')
                return redirect("dashboard:update_interest_view",interest_id=interest.id)
            else:
                print("form is not valid")
                print(interest_form.errors)   

        return render(request,"dashboard/update_interest.html",{"interest":interest})
    except Interest.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:interests_view')
    except Exception as e:
       messages.error(request, f"An error occurred: {str(e)}")
       return redirect('dashboard:interests_view')


# Projects views

def projects_view(request:HttpRequest):
   projects=Project.objects.all()
    
   if "search" in request.GET and len(request.GET["search"])>=1:
        projects = Project.objects.filter(name__icontains=request.GET["search"])

   if "order_by" in request.GET and request.GET["order_by"] == "created_at":
            projects=projects.order_by("-created_at")
    
   p=Paginator(projects,4)
   page=request.GET.get('page')
   projectobj=p.get_page(page)

   return render(request,"dashboard/projects.html",{'projects':projectobj})

def add_project_view(request:HttpRequest):
      
      if request.method=="POST":
        project_form=ProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
              project_form.save()
              print(Project.objects.all())
              messages.success(request, 'The project has been added successfully!')
              return redirect("dashboard:add_project_view")
        else:
            print("form is not valid")
            print(project_form.errors) 
            messages.error(request, 'The form not valid!')
            return redirect("dashboard:add_project_view")
              

      return render(request,"dashboard/add_project.html")


def delete_project_view(request:HttpRequest,project_id):
  try:
        project=Project.objects.get(pk=project_id)
        project.delete()
        return redirect('dashboard:projects_view')
  except Project.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:projects_view')
  except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('dashboard:projects_view')

def update_project_view(request:HttpRequest,project_id):
    try:  
        project=Project.objects.get(pk=project_id)
        if request.method=="POST":
            project_form=ProjectForm(request.POST,request.FILES,instance=project)
            if project_form.is_valid():
                project_form.save()
                messages.success(request, 'The project has been updated successfully!')
                return redirect("dashboard:update_project_view",project_id=project.id)
            else:
                print("form is not valid")
                print(project_form.errors)   

        return render(request,"dashboard/update_project.html",{"project":project})
    except Project.DoesNotExist:
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:projects_view')
    except Exception as e:
       messages.error(request, f"An error occurred: {str(e)}")
       return redirect('dashboard:projects_view')
    



# Memories views

def memories_view(request:HttpRequest):
   memories=Memory.objects.all()
    
   if "search" in request.GET and len(request.GET["search"])>=1:
        memories = Memory.objects.filter(title__icontains=request.GET["search"])

   if "order_by" in request.GET and request.GET["order_by"] == "created_at":
            memories=memories.order_by("-created_at")

   if "is_post" in request.GET and request.GET["is_post"] == 'True':
            memories=memories.filter(is_post=True)
   elif "is_post" in request.GET and request.GET["is_post"] == 'False':
            memories=memories.filter(is_post=False)

   if "category" in request.GET and request.GET["category"] == 'ACH':
            memories=memories.filter(category='ACH') 
   elif "category" in request.GET and request.GET["category"] == 'REL':
            memories=memories.filter(category='REL') 
   elif "category" in request.GET and request.GET["category"] == 'TRA':
            memories=memories.filter(category='TRA') 
   elif "category" in request.GET and request.GET["category"] == 'SPE':
            memories=memories.filter(category='SPE')  



   if "order_by" in request.GET and request.GET["order_by"] == "created_at":
            memories=memories.order_by("-created_at")        

    
   p=Paginator(memories,4)
   page=request.GET.get('page')
   memoobj=p.get_page(page)

   return render(request,"dashboard/memories.html",{'memories':memoobj,"CategoryChoices":Memory.CategoryChoices.choices})

def add_memo_view(request:HttpRequest):
      
      if request.method=="POST":
        project_form=MemoryForm(request.POST,request.FILES)
        if project_form.is_valid():
              project_form.save()
              print(Memory.objects.all())
              messages.success(request, 'The memory has been added successfully!')
              return redirect("dashboard:add_memo_view")
        else:
            print("form is not valid")
            print(project_form.errors) 
            messages.error(request, 'The form not valid!')
            return redirect("dashboard:add_memo_view")
              

      return render(request,"dashboard/add_memo.html",{"CategoryChoices":Memory.CategoryChoices.choices})


def delete_memo_view(request:HttpRequest,memo_id):
  try:
        memo=Memory.objects.get(pk=memo_id)
        memo.delete()
        return redirect('dashboard:memories_view')
  except Memory.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:memories_view')
  except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('dashboard:memories_view')

def update_memo_view(request:HttpRequest,memo_id):
    try:  
        memo=Memory.objects.get(pk=memo_id)
        if request.method=="POST":
            memo_form=MemoryForm(request.POST,request.FILES,instance=memo)
            if memo_form.is_valid():
                memo_form.save()
                messages.success(request, 'The memory has been updated successfully!')
                return redirect("dashboard:update_memo_view",memo_id=memo.id)
            else:
                print("form is not valid")
                print(memo_form.errors)   

        return render(request,"dashboard/update_memo.html",{"memo":memo,"CategoryChoices":Memory.CategoryChoices.choices})
    except Memory.DoesNotExist:
        messages.error(request, "An error occurred: The page not found")
        return redirect('dashboard:memories_view')
    except Exception as e:
       messages.error(request, f"An error occurred: {str(e)}")
       return redirect('dashboard:memories_view')    