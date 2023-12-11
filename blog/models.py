from django.db import models
from django.urls import reverse

# Create your models here.



class Blog(models.Model):
    image = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True) 


    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})