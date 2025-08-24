from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colecoes/', views.colecoes, name='colecoes'),
    path('kits/', views.kits, name='kits'),
    path('produtos/', views.produtos, name='produtos'),
]