# encrypted_file_manager/urls.py

from django.contrib import admin
from django.urls import path, include

# encrypted_file_manager/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('file_manager.urls')),
    path('accounts/', include('accounts.urls')),  # Include account URLs
]