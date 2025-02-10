from django.urls import path
from .views import (news_list_view, news_detail, category_news_list_view,
                    UpdateNewsView, DeleteNewsView, CreateNewsView)

app_name = 'news'


urlpatterns = (
    path('', news_list_view, name = 'news_list'),
    path('news/category/<int:category_id>', category_news_list_view, name = 'category_link'),
    path('news/<slug:news>', news_detail, name = 'news_detail'),
    path('news/<slug:slug>/update/', UpdateNewsView.as_view(), name = 'update_news'),
    path('news/<slug:slug>/delete/', DeleteNewsView.as_view(), name = 'delete_news'),
    path('news/create/', CreateNewsView.as_view(), name = 'create_news'),
)