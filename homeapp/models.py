from django.db import models

class homedata(models.Model):
    name = models.CharField(max_length=100)
    positin = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)
    email = models.EmailField()
    resume = models.FileField(upload_to='pdfs/')
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
