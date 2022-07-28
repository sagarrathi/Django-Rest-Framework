# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from django.htp import hhtp404
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field  = 'pk

    def perform_create(self, serializer):
        # print(serializer.validated_data)  
        title= serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        print("content is none")
        if content is None:
            content=title          
        serializer.save(content=content)

product_list_create_view=ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field  = 'pk

product_detail_view=ProductDetailAPIView.as_view()



class ProductListAPIView(generics.ListAPIView):
    """
    Not going to use this 
    because we will use list with create
    """
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field  = 'pk

product_list_view=ProductListAPIView.as_view()

@api_view(["GET","POST"])
def product_alt_view(request, *args, **kwargs):
    method=request.method
    if method=='GET':
        # list data 
        pass
    if method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #Raise expection provides frindly error
            # serializer.save() this creates the instance
            # ehile .data does not
            print("serializer.data",serializer.data)
            return Response(serializer.data)
        else: 
            return Response({"message":"title cannot be empty "})
