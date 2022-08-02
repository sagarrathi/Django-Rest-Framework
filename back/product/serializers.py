#Rest
from rest_framework import serializers
from rest_framework.reverse import reverse

#Api
from api.serializers import UserPublicSerializer

#Product
from .models import Product
from .validators import validate_title, validate_title_2


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',

    )
    title = serializers.CharField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
    owner=UserPublicSerializer(read_only=True, source='user')
    related_products=ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data=serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',

    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field='pk',

    )

    email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[validate_title, validate_title_2])

    name= serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            # 'my_user_data',
            'owner',
            'pk',
            'url',
            'edit_url',
            'email',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'related_products',
            
        ]

    def validate_title(self,value):
        value=str.title(value)
        return value

    # def get_my_user_data(self, obj):
    #     return {
    #         "username":obj.user.username
    #     }
    # # Obj is instance of object being called
    # Thuis prevents dynamic instacne whihc then have to be sourced

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    #     # return f"/api/products/{obj.pk}/"
    def create(self, validated_data):
        # return Product.object.create(**validated_data) default
        print("email field====>")
        email = validated_data.pop("email")
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        print("validated data", validated_data)
        email = validated_data.pop("email")
        return super().update(instance, validated_data)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        else:
            return obj.get_discount()
    
    
