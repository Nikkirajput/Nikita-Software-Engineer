from django.db import models

class services01data(models.Model):
    heading = models.CharField(max_length = 100)
    head_about = models.CharField(max_length=100)
    p_head = models.CharField(max_length=100)
    p_about = models.CharField(max_length=100)
    p_img = models.ImageField(upload_to='images/', null=True, blank=True)

class services02data(models.Model):
    card_head = models.CharField(max_length = 100)
    card_about = models.CharField(max_length=100)
    card_link = models.URLField(max_length=500)
    
    
        
   
    
    
