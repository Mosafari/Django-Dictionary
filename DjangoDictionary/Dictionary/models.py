from django.db import models

# Create your models here.
class Dictionary(models.Model):
    
    word = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255, default=None)
    targetlang = models.CharField(max_length=255, default=None)
    pronunciation = models.CharField(max_length=255, default=None)
    src = models.CharField(max_length=255, default=None)
    
    def __str__(self):
        return self.word
    