from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=1000)
    def __str__(self):
        return self.user_name