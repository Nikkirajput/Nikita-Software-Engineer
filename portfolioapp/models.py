from django.db import models

class part01data(models.Model):
    heading = models.CharField(max_length = 100)
    head_about = models.CharField(max_length=100)
    btn01 = models.CharField(max_length=100)
    btn02 = models.CharField(max_length=100)
    btn03 = models.CharField(max_length=100)
    

class part02data(models.Model):
    btn01_head = models.CharField(max_length=100)
    btn01_about = models.CharField(max_length=100)
    btn01_img = models.ImageField(upload_to='images/', null=True, blank=True)
    
class part03data(models.Model):
    btn02_head = models.CharField(max_length=100)
    btn02_about = models.CharField(max_length=100)
    btn02_img = models.ImageField(upload_to='images/', null=True, blank=True)
    
    
class part04data(models.Model):
    btn03_head = models.CharField(max_length=100)
    btn03_about = models.CharField(max_length=100)
    btn03_img = models.ImageField(upload_to='images/', null=True, blank=True)       
     
    
    
        
   
    
    
