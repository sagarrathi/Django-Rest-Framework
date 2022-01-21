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
    path("registration", views.registration, name="registration"),
    # path('cbv',views.TMView.as_view(), name="cbv"),
    path('cbv/<int:pk>/', views.SchoolDetailView.as_view(),name='detail'),
    path('cbv/', views.SchoolListView.as_view(),name='list' ),

    path('cbv/create', views.SchoolCreateView.as_view(),name='create' ),
    path('cbv/update/<int:pk>/', views.SchoolUpdateView.as_view(),name='update' ),
    path('cbv/delete/<int:pk>/', views.SchoolDeleteView.as_view(),name='delete' ),
    
    
]
