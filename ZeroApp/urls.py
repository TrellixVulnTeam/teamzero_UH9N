
from django.contrib import admin
from django.urls import path
from store.views import all_games
urlpatterns = [
    path('admin/', admin.site.urls),
]
