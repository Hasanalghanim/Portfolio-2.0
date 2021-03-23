from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Project(models.Model):

    Project_Title = models.CharField(max_length=100, )
    Project_info = models.TextField()
    stack = models.CharField(max_length=100, blank=True )
    image = ResizedImageField(size=[400, 300],
        upload_to='projects/images/', default='projects/images/default.jpg', quality=100)
    Project_URL = models.URLField(blank=True)

    def __str__(self):
        return self.Project_Title
