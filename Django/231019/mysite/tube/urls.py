from django.urls import path
from . import views

app_name = 'tube'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/comment/new/', views.comment_new, name='comment_new'),
    path('tag/<str:tag>/', views.post_tag_list, name='post_tag_list')
]