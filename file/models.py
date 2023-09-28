from django.db import models
from django.contrib.auth.models import User

class UploadFile(models.Model):
    name = models.CharField(default="File")
    description = models.TextField(default="")
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadFile, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class FileUserDetect(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadFile, null=True, on_delete=models.CASCADE)
    permit = models.BooleanField(default=True)
    comment_permission = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)