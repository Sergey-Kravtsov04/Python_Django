from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request,'main/main.html')
def log_reg(request):
    return render(request,'main/login.html')
def news(request):
    return render(request, 'main/news.html')
def about(request):
    return render (request,'main/about.html')
def reg(request):
    return render(request, 'main/registration.html')
