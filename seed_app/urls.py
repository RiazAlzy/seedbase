from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload/', views.upload_seed_view, name='upload_seed'),
    path('search/', views.search_seed_view, name='search_seed'),
    path('my-seeds/', views.my_seeds_view, name='my_seeds'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update-seed/<int:pk>/', views.update_seed_view, name='update_seed'),
    path('delete-seed/<int:pk>/', views.delete_seed_view, name='delete_seed'),
    path('register/', views.register_view, name='register'), # Add registration URL
]