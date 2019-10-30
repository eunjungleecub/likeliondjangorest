from django.db import models
from django.conf import settings

class Writing(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=50)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    files = models.FileField(blank=True,null=True, upload_to='files')
