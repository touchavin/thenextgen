from django.shortcuts import render
from rest_framework.response import Response
from .models import netxgen
from datetime import datetime
# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        company_name = request.POST['company_name']
        company_type = request.POST['company_type']
        interested_data = request.POST['interested_data']
        prefered_channel = request.POST['prefered_channel']
        ## save ข้อมูลลง ฐานข้อมูล 
        Customer_info = netxgen(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, company_name=company_name, company_type=company_type, interested_data=interested_data, prefered_channel=prefered_channel)
        Customer_info.save()
        

        return render(request,'home.html')
    return render(request, 'index.html')





   
def home(request):
    return render(request, 'home.html')