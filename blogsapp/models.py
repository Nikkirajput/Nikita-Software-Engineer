from django.db import models

class blog01data(models.Model):
    heading = models.CharField(max_length = 100)
    about = models.CharField(max_length=100) 

class blog02data(models.Model):
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    head = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    
    
class skilldata(models.Model):
    skill_rate = models.IntegerField()
    skill_name = models.CharField(max_length=100)
     
 
class footerdata(models.Model):
    copy_date = models.IntegerField()
    copy_name = models.CharField(max_length=100)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()