from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import pandas as pd
import plotly.express as px
from store.forms import ContactForm

def homepage(request):
    return render(request,"homepage.html")
def graph(request):
    return render(request, "graph.html")
def about_us(request):
    return render(request,"about_us.html")
def contact(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


    return render(request,"contact.html")
def all_games(request):
    df1 = pd.read_csv("static/data.csv", header=0)
    df1.columns=['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
    allData=[]
    for i in range(df1.shape[0]):
        temp=df1.loc[i]
        allData.append(dict(temp))
        context={'data':allData}
    return render(request,"all_games.html",context)

def plot1(request):
    df2 = pd.read_csv("static/data.csv", header=0)
    df2.columns = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales',
                  'Other_Sales', 'Global_Sales']
    allData = []
    for i in range(df2.shape[0]):
        temp = df2.loc[i]
        allData.append(dict(temp))
        context = {'data': allData}
    fig = px.pie(df2, values='Global_Sales', names='Platform', title='Total Global Sales for Each Platform')
    fig.show()
    return render(request,"graph.html",context)

def plot2(request):
    df3 = pd.read_csv("static/data.csv", header=0)
    df3.columns = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales',
                  'Other_Sales', 'Global_Sales']
    allData = []
    for i in range(df3.shape[0]):
        temp = df3.loc[i]
        allData.append(dict(temp))
        context = {'data': allData}
    fig = px.pie(df3, values='Global_Sales', names='Year', title='Total Global Sales for Each Year')
    fig.show()
    return render(request,"graph.html",context)

def plot3(request):
    df4 = pd.read_csv("static/data.csv", header=0)
    df4.columns = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales',
                  'Other_Sales', 'Global_Sales']
    allData = []
    for i in range(df4.shape[0]):
        temp = df4.loc[i]
        allData.append(dict(temp))
        context = {'data': allData}
    fig = px.pie(df4, values='Global_Sales', names='Genre', title='Total Global Sales for Each Genre')
    fig.show()
    return render(request,"graph.html",context)

