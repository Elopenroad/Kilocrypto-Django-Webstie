from django.db import models

# Create your models here.


class Panel(models.Model):
    coin_name = models.CharField(max_length=500)
    initial_price = models.IntegerField()
    current_price = models.IntegerField()
    ai_message = models.TextField()
