# Generated by Django 3.1.1 on 2020-10-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesys', '0004_auto_20201005_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_uploaded', models.FileField(upload_to='media/')),
            ],
        ),
    ]
