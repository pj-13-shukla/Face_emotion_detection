from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.forms import FaceRecognitionform
from app.machinelearning import pipeline_model
from django.conf import settings
from app.models import FaceRecognition 
# from app.forms import ImageForm
import os

# Create your views here.


def index(request):
    form = FaceRecognitionform()

    if request.method == 'POST':
        form = FaceRecognitionform(request.POST or None, request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)

            # extract the image object from database
            primary_key = save.pk
            imgobj = FaceRecognition.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT,fileroot)
            results = pipeline_model(filepath)
            print(results)


            return render(request,'index.html',{'form':form,'upload':True,'results':results})


    return render(request,'index.html',{'form':form,'upload':False})


# def image_upload_view(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('image_upload')
#     else:
#         form = ImageForm()
#     images = Image.objects.all()  # Fetch all image objects from the database
#     return render(request, 'image_upload.html', {'form': form, 'images': images})