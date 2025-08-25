from django.contrib import admin
from portfolioapp.models import  part01data,part02data,part03data,part04data
class part01Admin(admin.ModelAdmin):
    list_display = ( 'heading','head_about','btn01','btn02','btn03')

admin.site.register(part01data, part01Admin)

class part02Admin(admin.ModelAdmin):
    list_display = ( 'btn01_head','btn01_about','btn01_img')

admin.site.register(part02data, part02Admin)


class part03Admin(admin.ModelAdmin):
    list_display = ( 'btn02_head','btn02_about','btn02_img')

admin.site.register(part03data, part03Admin)


class part04Admin(admin.ModelAdmin):
    list_display = ( 'btn03_head','btn03_about','btn03_img')

admin.site.register(part04data, part04Admin)
