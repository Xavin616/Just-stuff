from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass

class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,related_name='author')
    image = models.ImageField(null=True, blank=True)
    topic = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    pubDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.id}: {self.topic}") 