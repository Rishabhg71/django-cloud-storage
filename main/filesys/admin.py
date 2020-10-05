from django.contrib import admin

# Register your models here.

from . models import upload_model
# ,upload_doc
admin.site.register(upload_model)
# admin.site.register(upload_doc)