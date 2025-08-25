from django.contrib import admin
from blogsapp.models import  blog01data,blog02data,skilldata,footerdata,Contact


class blog01Admin(admin.ModelAdmin):
    list_display = ( 'heading','about')

admin.site.register(blog01data, blog01Admin)

class blog02Admin(admin.ModelAdmin):
    list_display = ( 'img','head','date','about')

admin.site.register(blog02data, blog02Admin)

class skillAdmin(admin.ModelAdmin):
    list_display = ( 'skill_rate','skill_name')

admin.site.register(skilldata, skillAdmin)



class footerAdmin(admin.ModelAdmin):
    list_display = ( 'copy_date','copy_name')

admin.site.register(footerdata, footerAdmin)

admin.site.register(Contact)