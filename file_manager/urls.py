# file_manager/urls.py

from django.urls import path
from .views import upload_file, download_file, file_list, delete_file,custom_logout 
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', upload_file, name='upload_file'),
    path('download/<int:pk>/', download_file, name='download_file'),
    path('files/', file_list, name='file_list'),
    path('delete/<int:pk>/', delete_file, name='delete_file'),
    path('logout/', custom_logout, name='logout'),
]