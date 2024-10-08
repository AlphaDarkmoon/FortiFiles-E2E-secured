# file_manager/views.py

import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import EncryptedFile
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from encrypted_files.base import EncryptedFile as EncryptedFileHandler  # Import your decryption handler
from django.contrib.auth import logout
from django.urls import reverse

@login_required
def download_file(request, pk):
    encrypted_file_instance = get_object_or_404(EncryptedFile, pk=pk)
    
    if encrypted_file_instance.user != request.user:
        return render(request, 'file_manager/error.html', {'message': "You do not have permission to download this file."})

    # Decrypt the file before sending it to the user
    ef = EncryptedFileHandler(encrypted_file_instance.file)  # Assuming this class handles decryption
    response = HttpResponse(ef.read(), content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{encrypted_file_instance.file.name.split("/")[-1]}"'
    return response

@login_required
def delete_file(request, pk):
    file_instance = get_object_or_404(EncryptedFile, pk=pk)
    if file_instance.user == request.user:
        # Delete the file from the filesystem
        if file_instance.file:
            file_path = os.path.join(settings.MEDIA_ROOT, file_instance.file.name)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Remove the file from the filesystem

        file_instance.delete()  # Delete the instance from the database
        return redirect('file_list')  # Redirect to the file list after deletion
    
    return render(request, 'file_manager/error.html', {'message': 'You do not have permission to delete this file.'})

@login_required
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            encrypted_file_instance = EncryptedFile(user=request.user, file=uploaded_file)
            encrypted_file_instance.save()
            return redirect('file_list')  # Redirect to the file list after upload

    return render(request, 'file_manager/upload.html')  # Render the upload page

@login_required
def file_list(request):
    files = EncryptedFile.objects.filter(user=request.user)
    return render(request, 'file_manager/file_list.html', {'files': files})  # Render the template with context

def custom_logout(request):
    # Log out the user
    logout(request)
    # Redirect to the upload page
    return redirect(reverse('upload_file'))