from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.TodoListAPIView.as_view(), name='todo-list'),
    path('api/new/', views.TodoCreateAPIView.as_view(), name='todo-create'),
    path('api/<int:pk>/', views.TodoDetailAPIView.as_view(), name='todo-detail'),
    path('api/<int:pk>/delete/', views.TodoDeleteAPIView.as_view(), name='todo-delete'),
    path('api/<int:pk>/put/', views.TodoUpdateAPIView.as_view(), name='todo-update'),
]
