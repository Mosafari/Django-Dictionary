from django.db import models

# Create your models here.
class Dictionary(models.Model):
    
    word = models.CharField(max_length=255, unique=True)
    meaning = models.CharField(max_length=255)
    targetlang = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.word
    