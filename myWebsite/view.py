#from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def Contact(request):
    return render(request,"contact.html")

"""def Help(request):
    return HttpResponse("<h1>This is the Help page</h1>")"""
