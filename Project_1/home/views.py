from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is home page")


def aboutme(request):
    return render(request,'aboutme.html')

def contactme(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save() 
        messages.success(request, 'Successfully sent!')
        
    return render(request,'contactme.html')