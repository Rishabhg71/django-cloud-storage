# Generated by Django 3.1.1 on 2020-10-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesys', '0008_upload_model_user_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_model',
            name='file_uploaded',
            field=models.FileField(upload_to='media/<django.db.models.fields.CharField>'),
        ),
    ]
