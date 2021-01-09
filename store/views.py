from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from store.models import Games

def all_games(request):
    games_list = Games.objects.all()
    return render(request, "games.html", {'games_list': games_list})