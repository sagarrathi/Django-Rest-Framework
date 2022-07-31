
########## For Normal Template ########
from django.shortcuts import render
from django.http import HttpResponse
#######################################

###### For Forms Auto Poplate #########
from social.models import AccessRecord, Users
from social import forms
#######################################

################### For Login #########
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
#######################################


##### For Classe based view ###########
from social.models import School, Student
from django.views.generic import (View, TemplateView, 
                                    ListView, DetailView,
                                    CreateView,UpdateView,
                                    DeleteView
                                    )
from django.urls import reverse_lazy
#######################################



# Create your views here.
class CBView(View):
    def get(self, request):
        return HttpResponse("Jai Shri Ram")

class TMView(TemplateView):
    template_name='social/index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['temp_X']="Jai Shree Hanuman Ji Ki"
        return context

class SchoolListView(ListView):
    context_object_name="schools"
    model=School


class SchoolDetailView(DetailView):
    context_object_name="school_detail"
    model=School
    template_name='social/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name',)
    model=School


class SchoolUpdateView(UpdateView):
    fields=('principal',)
    model=School


class SchoolDeleteView(DeleteView):
    model=School
    success_url =reverse_lazy("social:list")



def index(request):
    webp_list=AccessRecord.objects.order_by('date')
    my_dict={
        "temp_X":"Ram Ji Ki Jai bolo",
        "access_record":webp_list
    }

    return render(request,'social/index.html',context=my_dict)

    # return HttpResponse("<h1>Hello world</h1>")

def user_login(request):

    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password') 

        user =authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('social:index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried but cannot login")
            print(username, password)
            return HttpResponse("Invalid details supplied")
        
    else:
        return render(request,'social/login.html', context={})

# Only login can enter
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('social:index'))

@login_required
def special(request):
    return HttpResponse("you are logged in")    

def registration(request):
    registered=False
    
    # Get form data
    if request.method =="POST":
        user_form=forms.UserForm(data=request.POST)
        profile_form=forms.UserProfileInfoForm(request.POST, request.FILES)
        
        # Check data is valid
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user.password) # For hashing passsword
            user.save()

            #Profile
            profile=profile_form.save(commit=False)
            profile.user=user

            print(request.FILES)
            # if 'picture' in request.FILES:
            #     profile.picture=request.FILES['picture']

            profile.save()

            registered=True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=forms.UserForm()
        profile_form=forms.UserProfileInfoForm()

    context_dict={
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered
        }
    
    return render(request,'social/registration.html', context=context_dict)










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


