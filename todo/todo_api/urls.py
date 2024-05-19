# todo_api/urls.py
from django.urls import path
from .views import TodoListApiView

urlpatterns = [
    path('api/', TodoListApiView.as_view(), name='todo_list'),  # Ensure there's a trailing slash
]
