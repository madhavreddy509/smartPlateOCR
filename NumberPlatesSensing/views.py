from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import os 
from deepLearning import OCR

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

def ocr(request):
    if request.method == 'POST':
        upload_file = request.FILES['image_name']
        filename = upload_file.name
        path_save = os.path.join(UPLOAD_PATH,filename)
        with open(path_save, 'wb') as destination:
            for chunk in upload_file.chunks():
                destination.write(chunk)
        text = OCR(path_save,filename)
        return render(request,'index.html',{'upload':True,'upload_image':filename,'text':text})
    return render(request,'index.html',{'upload':False})