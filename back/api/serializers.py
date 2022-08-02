#Rest
from rest_framework import serializers

#Django
from django.contrib.auth import get_user_model
User=get_user_model()

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',

    )
    title = serializers.CharField(read_only=True)



class UserPublicSerializer(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    # other_product=serializers.SerializerMethodField(read_only=True)

    # def get_other_product(self, obj):
    #     request=self.context.get('request')
    #     user=obj
    #     my_products_qs=user.product_set.all()
    #     return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data