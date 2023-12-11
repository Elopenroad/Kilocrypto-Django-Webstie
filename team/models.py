from django.db import models

# Create your models here.


class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=500)
    role = models.CharField(max_length=500)
    face_book = models.URLField(max_length=500)
    twitter = models.URLField(max_length=500)
    youtube = models.URLField(max_length=500)
    instagram = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)

    
    def __str__(self):
        return f"name : {self.name} role : {self.role}"
    

