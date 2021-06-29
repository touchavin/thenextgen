from django.contrib import admin
from.models import  netxgen

# Register your models here.
class netxgenAdmin(admin.ModelAdmin):
    list_display = ['Customer']
    list_filter = ['Customer']
    search_fields = ['Customer']


admin.site.register(netxgen, netxgenAdmin)