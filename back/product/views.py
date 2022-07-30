# Rest Framework
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

# API Related
from api.authentication import  TokenAuthentication 
# from api.permissions import StaffEditorPermission
from api.mixins import StaffEditorPermissionMixin, UserQuerysetMixin
# from api.permissions import StaffEditorPermission

# App related
from .models import Product
from .serializers import ProductSerializer


# Django related
# from django.http import Http404
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(
    UserQuerysetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        print("content is none")
        if content is None:
            content = title
        instance = serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kawrgs):
    #     qs=super().get_queryset(*args, **kawrgs)
    #     request =self.request 
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()  
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
  
product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(
    StaffEditorPermissionMixin,
    generics.ListAPIView):
    """
    Not going to use this 
    because we will use list with create
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
product_list_view = ProductListAPIView.as_view()


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDeleteAPIView.as_view()


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None,  *args, **kwargs):
    method = request.method
    if method == 'GET':
        if pk is not None:
            # Detail
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        # list data
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        # create data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)

        return Response({"message": "title cannot be empty "}, status=404)


class ProductMixinAPIView(
        StaffEditorPermissionMixin,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        generics.GenericAPIView
        ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs["pk"]
        if pk is not None:
            return retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        print("content is none")
        if content is None:
            content = "this is a single view doing cool stuff"
        instance = serializer.save(content=content)


product_mixin_view = ProductMixinAPIView.as_view()
