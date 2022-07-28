import json

from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

# @api_view(["POST"])
def api_home(request, *args, **kwargs):
    """ 

    DRF API View 
    """
    data=request.data
    return JsonResponse(data)
    # instance=Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data=ProductSerializer(instance).data
    # return Response(data)