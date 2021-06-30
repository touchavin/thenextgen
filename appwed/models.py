from django.db import models
from django.utils.html import format_html
# Create your models here.



    







class netxgen(models.Model):
    Day = models.DateField(auto_now_add=True, blank=True, null=True)
    Time = models.TimeField(auto_now_add=True, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_type = models.CharField(max_length=100, blank=True, null=True)
    interested_data = models.CharField(max_length=500, blank=True, null=True)
    prefered_channel = models.CharField(max_length=200, blank=True, null=True)
    
   
    