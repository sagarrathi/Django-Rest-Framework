from django.urls import path
from . import views

app_name="social"

urlpatterns = [
    path('', views.index, name="index"),
    path('help',views.help, name="help"),
    path('users', views.users, name="users"),
    path("forms", views.form_view, name="forms"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("registration", views.registration, name="registration")
    
]
