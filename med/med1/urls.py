from unicodedata import name
from django.contrib import admin
from django.urls import path
from med1 import views
from django.conf import settings  
from django.conf.urls.static import static 
urlpatterns = [
    path('',views.home,name="homepage"),
    path('registration',views.regis,name="registration"),
    path('prescription',views.prescrib,name="prescription"),
    path('record',views.record,name="record"),
    path('presmail',views.pres,name="mail"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
