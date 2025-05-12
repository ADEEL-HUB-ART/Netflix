from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, null=True, blank=True) 
    
    def __str__(self):
        return self.title