from django.contrib import admin
from aboutapp.models import aboutdata

class aboutAdmin(admin.ModelAdmin):
    list_display = ( 'img_forabout','work_experience','work_experience_detail','main_skills','skill_01','skill_01_detail','skill_02','skill_02_detail','skill_03','skill_03_detail','education','education_01','education_01_detail','education_02','education_02_detail','education_03','education_03_detail' ,'other' ,'other_01','other_01_detail','other_02','other_02_detail','other_03','other_03_detail')

admin.site.register(aboutdata, aboutAdmin)
