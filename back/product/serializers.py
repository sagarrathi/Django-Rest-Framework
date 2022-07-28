from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',    
        ]
    # Obj is instance of object being called
    # Thuis prevents dynamic instacne whihc then have to be sourced
    def get_my_discount(self, obj):
        return  obj.get_discount()
