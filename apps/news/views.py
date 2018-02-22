from django.shortcuts import render
from django.views import View

from .models import News


# Create your views here.

class NewsListView(View):
    def get(self, request):
        all_news = News.objects.all()
        sort = request.GET.get('sort', '')
        if sort == 'gs':
            all_news = all_news.filter(type=sort)
        if sort == 'hy':
            all_news = all_news.filter(type=sort)
        if sort == 'jt':
            all_news = all_news.filter(type=sort)
        return render(request, '资讯列表.html', {
            'all_news': all_news
        })

class NewsDetailView(View):
    def get(self,request,news_id):
        news = News.objects.get(id = int(news_id))

        return render(request,"资讯详情.html",{
            'news':news
        })
