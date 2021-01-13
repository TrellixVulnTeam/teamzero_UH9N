
from django.contrib import admin
from django.urls import path
from store.views import homepage,graph,about_us,all_games,contact,search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',contact),
    path('about_us/',about_us),
    path('graph/',graph),
    path('all_games/',all_games),
    path('homepage/',homepage),
    path('search/',search),
    
]
