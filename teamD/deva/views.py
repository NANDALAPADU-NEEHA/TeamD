from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
    return render(request,'srit.html')
def func2(request):
    return render(request,'app1/profile.html')
