
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to = 'portfolio/images/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title