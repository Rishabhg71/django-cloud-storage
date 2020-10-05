from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.allfiles,name='files'),
    path('fileupload',views.fileupload,name='fileupload'),
    path('fileuploading',views.fileuploading,name='fileuploading'),
]