from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')

def home(request):
    return render(request, 'base.html', context={
        'title': 'Home',
    })
