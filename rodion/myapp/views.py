from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadFileForm()
    
    files = UploadedFile.objects.order_by('-uploaded_at')
    return render(request, 'home.html', {'form': form, 'files': files})
