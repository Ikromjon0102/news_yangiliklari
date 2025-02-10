from audioop import reverse
from venv import create

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView, CreateView

from .models import Category, News, Photos
from .forms import UpdateNewsForm, CreateNewsForm


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


class UpdateNewsView(UpdateView):
    model = News
    fields = ('title', 'body', 'category', 'image','status')
    template_name = 'crud/update.html'


# class UpdateNewsView(View):
#
#     def get(self, request, news):
#         news = News.objects.get(slug = news)
#         form = UpdateNewsForm(instance=news)
#
#         context = {
#             'news':news,
#             'form':form
#         }
#         return render(request, 'crud/update.html', context)
#
#     def post(self, request, news):
#         news = News.objects.get(slug = news)
#         form = UpdateNewsForm(
#             instance=news,
#             data=request.POST,
#             files = request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('news_list')
#
#         context = {
#             'news':news,
#             'form':form
#         }
#         return render(request, 'crud/update.html', context)
#


class DeleteNewsView(DeleteView):
    model = News
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('news_list')

# class DeleteNewsView(View):
#     def get(self, request, news):
#         news = News.objects.get(slug = news)
#         news.delete()
#         return redirect('news_list')



class CreateNewsView(CreateView):
    model = News
    fields = ['title', 'slug', 'category', 'body', 'image', 'status']
    template_name = 'crud/create.html'

# class CreateNewsView(View):
#     def get(self, request):
#         form  = CreateNewsForm
#
#         context = {
#             'form':form
#         }
#         return render(request, 'crud/create.html', context)
#
#     def post(self, request):
#         form = CreateNewsForm(data=request.POST,
#                               files=request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('news_list')
#
#         context = {
#             'form': form
#         }
#         return render(request, 'crud/create.html', context)
#

