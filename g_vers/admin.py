from django.contrib import admin
from g_vers.models import *


class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'upload_by', 'upload_date', 'upload_date')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'address', 'message')


admin.site.register(Song)
admin.site.register(Photography, PhotographyAdmin)
admin.site.register(Contact, ContactAdmin)
