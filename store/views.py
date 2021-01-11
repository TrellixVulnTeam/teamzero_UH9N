from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def homepage(request):
    return render(request,"homepage.html")
def account(request):
    return render(request,"account.html")
def about_us(request):
    return render(request,"about_us.html")
def contact(request):
    return render(request,"contact.html")
def all_games(request):
    return render(request,"all_games.html")