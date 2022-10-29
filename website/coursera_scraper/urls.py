from django.urls import path
from coursera_scraper import views

urlpatterns = [
    path('', views.index, name='index'),
]