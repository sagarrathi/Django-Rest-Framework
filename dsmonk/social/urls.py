from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('help',views.help, name="help"),
    path('users', views.users, name="users"),
    path("forms", views.form_view, name="forms")
]
