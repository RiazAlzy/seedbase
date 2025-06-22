from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload/', views.upload_seed_view, name='upload_seed'),
    path('search/', views.search_seed_view, name='search_seed'),
]