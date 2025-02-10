from django import forms

from news_app.models import News


class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','category','body', 'image']


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'category', 'body', 'image', 'status']