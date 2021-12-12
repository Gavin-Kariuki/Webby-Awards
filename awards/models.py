from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=320)
    link = models.URLField(max_length=60)
    date = models.DateField(auto_now=True)
    screen_one = CloudinaryField('image')
    screen_two = CloudinaryField('image')

    class Meta:
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name

    @classmethod
    def search_project(cls,word):
        searched = cls.objects.filter(name__icontains = word)
        return searched

class Profile(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)

    class Meta:
        ordering = ['-image']

class Votes(models.Model):
    

