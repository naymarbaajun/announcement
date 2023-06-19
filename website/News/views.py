from django.shortcuts import render
from django.http import HttpResponse
from .models import announcement



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def form(request):
    return render(request, 'form.html')

def news(request):
    annouc = announcement.objects.all()
    return render(request, "news.html", {'annoc':annoc})

def academic(request):
    return render(request, 'academic.html')

def event(request):
    return render(request, 'event.html')

def loan(request):
    return render(request, 'loan.html')        