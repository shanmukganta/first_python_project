from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'signup.html',{'name':"shanmuk"})
def hi(request):
    k = request.GET['username']
    k=k.upper()
    return render(request,'submit.html',{'l':k})

 