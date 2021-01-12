from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import pandas as pd
from django.db.models import Q
from store.models import Games

def homepage(request):
    return render(request,"homepage.html")
def account(request):


    return render(request,"account.html")
def about_us(request):
    return render(request,"about_us.html")
def contact(request):
    return render(request,"contact.html")
def all_games(request):
    df = pd.read_csv("static/data.csv", header=0)
    df.columns=['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
    allData=[]
    for i in range(df.shape[0]):
        temp=df.loc[i]
        allData.append(dict(temp))
        context={'data':allData}
    return render(request,"all_games.html",context)

def game(request):
    return render(request, "game.html")

def search(request):
    query=request.GET.get('q','')
    if query:
        queryset=(Q(Games.Name__contains==query))
        results = allData.objects.filter(queryset).distinct()



    return render(request,'search.html',{'results':results,'query':query})


