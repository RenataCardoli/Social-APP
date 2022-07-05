from datetime import date
from importlib.resources import contents
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)
    
    def comments_count(self):
        return self.comments_set.all().count()
    
    def comment(self):
        return self.comment_set.all()
    
    def __str__(self):
        return self.title
    
    
opciones_consultas= [
    [0, "Contact"],
    [1, "Complaint"],
    [2, "Suggestion"],
    [3, "Kudos"]
]

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_contact = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.name
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.content
    
