from django.contrib import admin
from.models import  netxgen

# Register your models here.
class netxgenAdmin(admin.ModelAdmin):
    list_display = ['Day', 'Time', 'first_name', 'last_name', 'email', 'phone_number', 'company_name', 'company_type', 'interested_data', 'prefered_channel']
    list_filter = ['first_name']
    search_fields = ['first_name']


admin.site.register(netxgen, netxgenAdmin)