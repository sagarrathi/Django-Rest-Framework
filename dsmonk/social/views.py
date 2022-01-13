from django.shortcuts import render

from social.models import Topic, Webpage, AccessRecord, Users
from social import forms

# Create your views here.
from django.http import HttpResponse

def index(request):
    webp_list=AccessRecord.objects.order_by('date')
    my_dict={
        "temp_X":"Ram Ji Ki Jai bolo",
        "access_record":webp_list
    }

    return render(request,'social/index.html',context=my_dict)

    # return HttpResponse("<h1>Hello world</h1>")
def help(request):
    my_dict={"temp_X":"Ram Ji Ki Jai bolo"}
    return render(request,'social/help.html',context=my_dict)


def users(request):
    user_list=Users.objects.all()
    my_dict={"users":user_list}
    return render(request, 'social/users.html', context=my_dict)

def form_view(request):
    
    my_dict={"form":forms.UserModelForm()}

    
    if request.method=="POST":
        form=forms.UserModelForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            print("Validation sucessful")
            print(form.cleaned_data)
            print(form.errors)
            return index(request)
        
        my_dict["form"]=form
          
    return render(request,'social/forms.html', context=my_dict)

def login(request):
    
    my_dict={"userform":forms.UserProfileInfoForm()}

    
    if request.method=="POST":
        form=forms.UserProfileInfoForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            print("Validation sucessful")
            print(form.cleaned_data)
            print(form.errors)
            return index(request)
        
        my_dict["userform"]=form
          
    return render(request,'social/login.html', context=my_dict)

def logout(request):
    return render(request,'social/logout.html', context={})

def registration(request):
    return render(request,'social/registration.html', context={})
