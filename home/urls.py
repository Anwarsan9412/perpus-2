from django.urls import path
from .views import HomeView, CategoryView,Search

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('category/<pk>/', CategoryView, name='category'),
    path('search/', Search, name='search'),
    
]
