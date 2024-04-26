from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
from django.contrib import messages

def home(request):
    short_url=''
    url=''
    
    if request.method=="POST":
        url= request.POST.get("url")
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        #print(short_url)
        messages.success(request,"Short URL generated..!")
    context={
        "url":url,
        "short_url":short_url
    }
    return render(request,'index.html',context)
    