from django.shortcuts import render
from rest_framework.response import Response
from .models import netxgen

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
        Customer = request.POST['Customer']

        
        Customer_info = netxgen(Customer=Customer)
        Customer_info.save()
        
        
        

        ## save ข้อมูลลง ฐานข้อมูล 
        return render(request,'home.html')
    return render(request, 'index.html')





   
def home(request):
    return render(request, 'home.html')