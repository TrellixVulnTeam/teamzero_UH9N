from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import pandas as pd

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

