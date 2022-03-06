from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def logi(request):
    return render(request,'login.html')

def signi(request):
    return render(request,'signup.html')



# Create your views here.
