from django.contrib import admin
from otherapp.models import services01data,services02data

class services01Admin(admin.ModelAdmin):
    list_display = ( 'heading','head_about','p_head','p_about','p_img')

admin.site.register(services01data, services01Admin)


class services02Admin(admin.ModelAdmin):
    list_display = ( 'card_head','card_about','card_link')

admin.site.register(services02data, services02Admin)