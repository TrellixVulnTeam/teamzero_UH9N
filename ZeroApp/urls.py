
from django.contrib import admin
from django.urls import path
from store.views import homepage,about_us,all_games,contact,plot1,plot2,graph,plot3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',contact),
    path('about_us/',about_us),
    path('graph/',graph),
    path('graph1/',plot1),
    path('graph2/',plot2),
    path('graph3/',plot3),
    path('all_games/',all_games),
    path('',homepage),

]
