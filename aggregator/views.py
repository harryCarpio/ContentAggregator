from django.shortcuts import render, redirect
from .models import News


def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'aggregator/news.html', context)


def urlClickTracking(request, pk):
    news = News.objects.get(id=pk)
    news.track_click
    return redirect(news.link)
