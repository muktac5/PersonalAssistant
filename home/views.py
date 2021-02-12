from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"intro.html")
def login(request):
    return render(request,"login.html")
def register(request):
   return render(request,"register.html")
def forgot(request):
       return render(request,"forgot-password.html")
def home(request):
    return render(request,"main\index.html")
def family(request):
    return render(request,"family.html")
def work(request):
    return render(request,"work.html")
def health(request):
    return render(request,"health.html")
