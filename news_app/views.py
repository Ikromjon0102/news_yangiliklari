from django.shortcuts import render
from .models import Category, News, Photos


def news_list_view(request):
    news_list = News.objects.all()
    lastest_news = News.objects.all().order_by('-created_time')[:5]
    local_news = News.objects.filter(category__name = 'Mahalliy').order_by('-created_time')[:5]
    techno_news = News.objects.filter(category__name = 'Texnologiya')[:5]
    siyosiy_news = News.objects.filter(category__name = 'Siyosiy')[:5]
    sport_news = News.objects.filter(category__name = 'Sport')[:5]
    xorij_news = News.objects.filter(category__name = 'Xorij')[:5]
    photos = Photos.objects.all()[:6]
    category_list = Category.objects.all()



    context = {
        'news_list':news_list,
        'lastest_news':lastest_news,
        'local_news':local_news,
        'techno_news':techno_news,
        'siyosiy_news':siyosiy_news,
        'sport_news':sport_news,
        'xorij_news':xorij_news,
        'photos':photos,
        'category_list':category_list,
    }

    return render(request, 'index.html', context)

def news_detail(request, news):
    yangilik = News.objects.get(slug = news)
    category_list = Category.objects.all()
    context = {
        'news': yangilik,
        'category_list': category_list,
    }

    return render(request, 'single_page.html', context)



def category_news_list_view(request, category_id):
    category = Category.objects.get(id = category_id)
    news_list = News.objects.filter(category__name=category.name)
    category_list = Category.objects.all()
    lastest_news = News.objects.all().order_by('-created_time')[:5]

    context = {
        'news_list':news_list,
        'category':category,
        'category_list':category_list,
        'lastest_news': lastest_news,
    }

    return render(request, 'category_news.html', context)


def category_list_view(request):
    category_list = Category.objects.all()

    return render(request, 'base.html', {'category_list':category_list})