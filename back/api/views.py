import json

from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """ 

    DRF API View 
    """
    if request.method  != 'GET':
        return Response({"detail":" Only GET allowed"}, status=405)
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        data=ProductSerializer(instance).data
    return Response(data)