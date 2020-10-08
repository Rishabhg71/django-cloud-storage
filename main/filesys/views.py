from django.http import HttpResponse
from django.shortcuts import render
from .forms import uploadform
from .models import upload_model
# ,upload_doc
from django.shortcuts import redirect
from django.views.static import serve
import os
from home.urls import urlpatterns
from django.urls import path
from home import views as views

def allfiles(request):
    # return render(request,'index.html',params)
    return render(request,'filesys/files.html')



def fileupload(request):
    print(request.session.get('username'))
    form = uploadform()  
    return render(request,'filesys/fileupload.html',{'form':form})




def handle_uploaded_file(f,user_folder,path):  
    # with open( 'media/'+ user_folder + '/'+f.name, 'wb+') as destination:  
    with open( str(path) + '/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():  
            destination.write(chunk)


def fileuploading(request):  
    if request.method == 'POST':  
        form = uploadform(request.POST, request.FILES)
        # upload_model.user_name = request.session.get('username')
        # print('session uname',upload_model.user_name)
        # file1 = upload_model(user_folder=request.session.get('username'),file_name=request.FILES['file_to_upload'].name,file_uploaded=request.FILES['file_to_upload'])
        # file1.save()
        try:
            if form.is_valid():
                print('form vaild') 
                handle_uploaded_file(request.FILES['file_to_upload'], request.session.get('username'),request.POST.get('folder'))
                # handle_uploaded_file(request.FILES['file'])  
                return redirect('../index/'+ request.POST.get('folder'))
                # return HttpResponse("File uploaded successfuly")  
            else:  
                form = uploadform()  
                return render(request,"index.html",{'form':form})
        except Exception as e:
            return HttpResponse(str(e))
            # return HttpResponse("maybe file is uploaded but exeption occured")




def makefolder(request):
    folder = request.POST.get('folder_create_name')
    # print()
    os.mkdir('media/'+ request.session.get('username') + '/' + folder)    
    urlpatterns.append(path('media/'+ request.session.get('username') + '/' + folder,views.folder,name='folder'))
    print('redirecting to ', '../index/'+ request.POST.get('folder'))
    if request.POST.get('folder') == request.session.get('username'):
        return redirect('../index/')
    else:
        return redirect('../index/'+ request.POST.get('folder'))



def download(request):
    filepath = 'media' 
    return serve(request, os.path.basename(filepath),os.path.dirname(filepath))


    