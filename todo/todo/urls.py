# todo/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include('todo_api.urls')),  # Ensure this line correctly points to your app's URLs
]
