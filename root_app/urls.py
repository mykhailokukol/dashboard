from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserViewSet.as_view({
        'post': 'create',
        'get': 'list',
    })),
    path('users/<int:pk>/', views.UserViewSet.as_view({
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy'
    })),
]