from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',

    )

    edit_url=serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field='pk',

    )
    class Meta:
        model = Product
        fields = [
            'pk',
            'url',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    # Obj is instance of object being called
    # Thuis prevents dynamic instacne whihc then have to be sourced

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    #     # return f"/api/products/{obj.pk}/"

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        else:
            return obj.get_discount()
