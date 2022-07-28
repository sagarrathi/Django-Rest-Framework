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
    if serializer.is_valid(raise_exception=True): #Raise expection provides frindly error
        # serializer.save() this creates the instance
        # ehile .data does not
        print("serializer.data",serializer.data)
        return Response(serializer.data)
    else:
        return Response({"message":"title cannot be empty "})