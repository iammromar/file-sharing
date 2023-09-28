from django.contrib import admin
from .views import UploadFile, Comment, FileUserDetect

# Register your models here.
admin.site.register(UploadFile)
admin.site.register(Comment)
admin.site.register(FileUserDetect)


