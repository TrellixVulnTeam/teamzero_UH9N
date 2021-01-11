
from django.contrib import admin
from django.urls import path
from store.views import homepage,account,about_us,all_games,contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',contact),
    path('about_us/',about_us),
    path('account/',account),
    path('all_games/',all_games),
    path('homepage/',homepage),
]
