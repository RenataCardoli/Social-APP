from django.urls import path
from .import views


urlpatterns = [
    path('social/', views.index , name='social-index'),
    path('about/', views.about , name='social-about'),
    path('post_detail/<int:pk>/', views.post_detail, name='social-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='social-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='social-post-delete'),
]
