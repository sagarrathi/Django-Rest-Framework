import json

from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """ 

    DRF API View 
    """
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance=serializer.save()
        print("saved data",instance)
        return Response(serializer.data)
    # instance=Product.n objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data=ProductSerializer(instance).data
    # return Response(data)