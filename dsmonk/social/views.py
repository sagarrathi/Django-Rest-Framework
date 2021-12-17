from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    my_dict={"temp_X":"Ram Ji Ki Jai bolo"}
    return render(request,'social/index.html',context=my_dict)

    # return HttpResponse("<h1>Hello world</h1>")
def help(request):
    my_dict={"temp_X":"Ram Ji Ki Jai bolo"}
    return render(request,'social/help.html',context=my_dict)
