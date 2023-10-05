from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('free/', views.free, name='free'),
    path('free/<int:pk>/', views.freedetail, name='freedetail'),
    path('oneone/', views.oneone, name='oneone'),
    path('oneone/<int:pk>/', views.oneonedetail, name='oneonedetail'),
]
