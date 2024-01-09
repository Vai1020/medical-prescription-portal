from datetime import date
from os import name
from django.contrib import auth
from tkinter.messagebox import RETRY
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse, request
from django.shortcuts import render,HttpResponseRedirect,redirect
from med1.models import prescribe
from med1.models import regis as registration
from med1.models import prescribe as pesc
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import EmailMultiAlternatives
from med.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
def home(request):
    return render(request,'home.html')


def regis(request):
    if request.method=="POST":
        try:
           image=request.FILES["image"]
        except MultiValueDictKeyError:
            image = False
        name=request.POST.get('name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        regis_number=request.POST.get('regis_number')
        password=request.POST.get('password')
        password = make_password(password)
        new1=registration.objects.create(name=name,last_name=last_name,phone=phone,email=email,regis_number=regis_number,password=password,image=image)
        new1.save()
        return render(request,'login.html')
    else:
        return render(request,'form.html')

    
def prescrib(request):
     if request.method=="POST":
         user=request.COOKIES['email']
         if user:
           name=request.POST.get('name')
           email=request.POST.get('email')
           date=request.POST.get('date')
           age=request.POST.get('age')
           gender=request.POST.get('gender')
           allergy=request.POST.get('allergy')
           medic=request.POST.get('medic')
           time=request.POST.get('time')
           desc=request.POST.get('desc')
           pesc1=pesc.objects.create(name=name,email=email,date=date,age=age,gender=gender,allergy=allergy,medic=medic,time=time,desc=desc)
           pesc1.save()
           entries=pesc.get_all_records()
           data={}
           data['entries']=entries
           html_content= render_to_string("presmail.html",data)
           text_content=strip_tags(html_content)
           email=EmailMultiAlternatives("testing",text_content,settings.EMAIL_HOST_USER,[email])
           email.attach_alternative(html_content,"text/html")
           email.send()
           return render(request,'prescription.html')
         else:
            return render(request,'prescription.html')
     else:
         return render(request,'prescription.html')

def record(request):
    entries=pesc.get_all_records()
    data={}
    data['entries']=entries
    return render(request,'history.html',data)

'''def mail(request):
    entries=pesc.get_all_records()
    data={}
    data['entries']=entries
    html_content= render_to_string("presmail.html",data)
    text_content=strip_tags(html_content)
    email=EmailMultiAlternatives("testing",text_content,settings.EMAIL_HOST_USER,["vaibhavdixit878@gmail.com"])
    email.attach_alternative(html_content,"text/html")
    email.send()'''

def pres(request):
    entries=pesc.get_all_records()
    data={}
    data['entries']=entries
    return render(request,'presmail.html',data)

def login(request):
        if request.method=="POST":
            email=request.POST.get('email')
            password=request.POST.get('password')
            y=registration.objects.filter(email=email).first()
            print(y.password)
            check=check_password(password,y.password)
            print(check)
            error_message = None
            if y:
                flag=check_password(password,y.password)
                print("one")
                if flag:
                      hello=render(request,'continue.html')
                      hello.set_cookie('email',email)
                      print("onee")
                      return hello
                else:
                    error_message = 'Email or Password invalid !!'
            else:
                error_message = 'Email or Password invalid !!'
            print(email, password)
            return render(request, 'login.html', {'error': error_message})
        else:
             return render(request, 'login.html')

def conti(request):
    if request.method=="GET":
     name=request.COOKIES['email']
    return render(request,'home.html',{'name':name})

def logout(request):
    bye=render(request,'home.html')
    bye.delete_cookie('email')
    return bye