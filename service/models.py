from django.db import models
from django.urls import reverse

# Create your models here.



class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True) 

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})