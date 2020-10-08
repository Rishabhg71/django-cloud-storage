
from django.urls import path,include
from . import views
import os

def folder_init(dir):
    folder_list = []
    indir = os.listdir(dir)
    for i in indir:
        full_path = str(dir) + "/" + str(i)
        if os.path.isdir(full_path):
            folder_list.append(full_path)
    
    return folder_list

def folder_tree(root):
    one_more_down_dir = folder_init(root)
    for i in one_more_down_dir:
            for folder_item in folder_init(i):
                one_more_down_dir.append(folder_item)
    # print(one_more_down_dir)
    return one_more_down_dir


media_urls = folder_tree('media')
media_urls_list_append = []
for i in folder_tree('media'):
    media_urls_list_append.append(path(str(i),views.folder,name=str(i)))

print(media_urls_list_append)







urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout')
]
urlpatterns.extend(media_urls_list_append)
#  + media_urls_list_append

# print(urlpatterns)