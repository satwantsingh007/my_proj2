from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title