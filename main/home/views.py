from django.http import HttpResponse
from django.shortcuts import render
from .models import users

from main.settings import MEDIA_ROOT,BASE_DIR
import os

def index(request):
    # return render(request,'index.html',params)
    return render(request,'home/index.html')



def signup(request):
    # return render(request,'index.html',params)
    user_name = request.POST.get('user_name')
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
    # return render(request,'index.html',params)
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
    

    try:
        user_name = request.session.get('username')
        path = MEDIA_ROOT + '/' + user_name
        files = os.listdir(path)
        params = {"files":files,'user_name':user_name}    
    except:
        return HttpResponse('something went wrong')
    
    # return render(request,'index.html',params)
    return render(request,'home/dashboard.html',params)



# to add new user 

# user = users(user_name="rishabh",user_password='12345678')
# user.save()