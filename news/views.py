from django.shortcuts import render
from .models import Articles


def news_main(request):
    news = Articles.objects.all()
    return render(request, 'news/news_main.html', {'news': news})
