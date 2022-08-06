import random

# Django
from django.conf import settings
from django.db import models
from django.db.models import Q


# Create your models here.
User =settings.AUTH_USER_MODEL #auth.user

TAGS_MODELS_VALUES=['ELEC','CAR','BOAT']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup= Q(title__icontains=query)
        qs=self.is_public().filter(lookup)
        if user is not None:
            qs_user= self.filter(user=user).filter(lookup)
            qs=(qs | qs_user).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Product(models.Model):
    user=models.ForeignKey(User, default=1,null=True,  on_delete=models.SET_NULL) 
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120, null=True) 
    price=models.DecimalField(max_digits=12, decimal_places=2, default=99.99)
    public=models.BooleanField(default=True)
    # publish_timestamp=models.DateField()

    objects=ProductManager()

    @property
    def body(self):
        return self.content
        
    def is_public(self) ->bool:
        return self.public
        
    def get_tags_list(self):
        return [random.choice(TAGS_MODELS_VALUES)]

        
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) *0.8)


    def get_discount(self):
        return "%.2f" %(float(self.price) *0.8)
    