from django.urls import path
from .views import news_list_view, news_detail, category_news_list_view

urlpatterns = (
    path('', news_list_view, name = 'news_list'),
    path('news/category/<int:category_id>', category_news_list_view, name = 'category_link'),
    path('news/<slug:news>', news_detail, name = 'news_detail'),
)