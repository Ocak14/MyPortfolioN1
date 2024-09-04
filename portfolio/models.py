from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation

 
class Index(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"


class Service(models.Model):
    image = models.ImageField(upload_to='Images/service')
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    image = models.ImageField(upload_to='Images/about')
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    


   