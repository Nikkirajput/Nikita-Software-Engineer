from django.db import models

class aboutdata(models.Model):
    img_forabout = models.ImageField(upload_to='images/', null=True, blank=True)
    work_experience = models.CharField(max_length=500)
    work_experience_detail = models.CharField(max_length=1000)
    
    main_skills = models.CharField(max_length = 100)
    skill_01 = models.CharField(max_length=100)
    skill_01_detail = models.CharField(max_length=100)
    skill_02 = models.CharField(max_length=100)
    skill_02_detail = models.CharField(max_length=100)
    skill_03 = models.CharField(max_length=100)
    skill_03_detail = models.CharField(max_length=100)
    
    education = models.CharField(max_length = 100)
    education_01 = models.CharField(max_length=100)
    education_01_detail = models.CharField(max_length=100)
    education_02 = models.CharField(max_length=100)
    education_02_detail = models.CharField(max_length=100)
    education_03 = models.CharField(max_length=100)
    education_03_detail = models.CharField(max_length=100)
    
    other = models.CharField(max_length = 100)
    other_01 = models.CharField(max_length=100)
    other_01_detail = models.CharField(max_length=100)
    other_02 = models.CharField(max_length=100)
    other_02_detail = models.CharField(max_length=100)
    other_03 = models.CharField(max_length=100)
    other_03_detail = models.CharField(max_length=100)
    
    
    # def __str__(self):
    #     return self.name
