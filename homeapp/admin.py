from django.contrib import admin
from homeapp.models import homedata

class homeAdmin(admin.ModelAdmin):
    list_display = ('name', 'positin', 'about','email', 'resume', 'profile_pic')

admin.site.register(homedata, homeAdmin)
