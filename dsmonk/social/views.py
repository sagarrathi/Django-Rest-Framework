from django.shortcuts import render

from social.models import Topic, Webpage, AccessRecord, Users


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

