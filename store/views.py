from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def homepage(request):
    return render(request,"homepage.html")