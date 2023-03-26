from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news_main'),
    path('add', views.add, name='add')
]