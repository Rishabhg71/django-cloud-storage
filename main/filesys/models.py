from django.db import models

# Create your models here.


class upload_model(models.Model):
    user_folder = models.CharField(max_length=50)
    user_name = None
    file_name = models.CharField(max_length=500)
    # file_uploaded = models.FileField(upload_to='media/'+ str(user_folder))
    # upload_path = str(user_folder)
    file_uploaded = models.FileField(upload_to='media/')

    def __str__(self):
        return file_name



class upload_doc(models.Model):
    file_uploaded = models.FileField(upload_to='media/')

    def __str__(self):
        return self.file_uploaded