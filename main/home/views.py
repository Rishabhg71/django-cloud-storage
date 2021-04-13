from django.http import HttpResponse
from django.shortcuts import render
from .models import users
from django.shortcuts import redirect

from main.settings import MEDIA_ROOT,BASE_DIR
import os

def index(request):
    return render(request,'home/index.html')



def signup(request):
    user_name = request.POST.get('user_name')
    if ' ' in user_name:
        return HttpResponse('dont use spaces in username')
    user_email = request.POST.get('user_email')
    pass_by_user = request.POST.get('pass')
    pass_by_user_again = request.POST.get('pass_again')
    if pass_by_user == pass_by_user_again:
        user = users(user_name=user_name,user_email=user_email,user_password=pass_by_user)
        user.save()
        try:
            path = os.path.join(MEDIA_ROOT,str(user_name))
            os.mkdir(path)
        except:
            print('cant make folder')
        params = {'message':'user created successfully'}
    else:
        params = {'message':'user not created something went wrong'}
    return render(request,'home/signup.html',params)



def login(request):
    user_name = request.POST.get('user_name')
    pass_by_user = request.POST.get('pass')
    user = users.objects.get(user_name=user_name)
    if user_name == user.user_name and pass_by_user == user.user_password:
        request.session['username'] = user_name
        print('logged in')
    else:
        params = {'uname':None,'upass':None}
        print('passkey didnt match')

    
    return render(request,'home/loggedin.html')




def dashboard(request):
    
    if request.session.get('username',False):
        print("session set")
        try:
            user_name = request.session.get('username')
            path = MEDIA_ROOT + '/' + user_name
            files = os.listdir(path)
            file_list = []
            directory = []
            for i in files:
                dst = 'media/' + user_name +'/' + str(i)
                print(dst)
                if os.path.isdir(dst):
                    directory.append(i)
                else:
                    file_list.append(i)
            params = {"files":file_list,'user_name':user_name,"directory":directory,"upload_dir":'media/'}    
        except:
            return HttpResponse('something went wrong')
        return render(request,'home/dashboard.html',params)
    else:
        return HttpResponse('session not set')

def folder(request):
    
    print(request.session.get('username',False))
    if request.session.get('username',False):
        path = str(request.get_full_path())
        # for i in 
        path = path.split('index/')
        files = os.listdir(path[1])
        file_list = []
        directory = []
        for i in files:
            if os.path.isdir(path[1] + '/' + i):
                directory.append(i)
            else:
                file_list.append(i)
        params = {"files":file_list,
        'user_name':request.session.get('username'),
        "directory":directory,
        "upload_dir":path[1]}    
        return render(request,'home/folder_init.html',params)
    else:
        print('session not set')
        return HttpResponse('session not set')


def logout(request):
    del request.session['username']
    return redirect('/index')


