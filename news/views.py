from django.shortcuts import render, get_object_or_404
from .models import News, Token
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def read_news(request, news_id):
    # Xəbəri tapmaq
    news = get_object_or_404(News, id=news_id)

    # Token modelini tapmaq və ya yaratmaq
    token, created = Token.objects.get_or_create(user=request.user)

    # Token əlavə etmək
    token.add_tokens(10)  # Hər bir xəbər oxunduqda 10 token veririk

    # Xəbəri oxumaq və göstərmək
    return render(request, 'news/detail.html', {'news': news})

# Əsas səhifə
def home(request):
    latest_news = News.objects.all().order_by('-published_date')  # Ən son xəbərləri alır
    return render(request, 'news/home.html', {'latest_news': latest_news})

# Xəbərin tam məlumatını göstərən səhifə
def news_detail(request, id):
    news_item = News.objects.get(id=id)  # Müraciət edilən xəbəri alır
    return render(request, 'news/news_detail.html', {'news_item': news_item})

def index(request):
    # Son 5 xəbəri göstərmək üçün
    latest_news = News.objects.all().order_by('-published_date')[:5]
    return render(request, 'news/home.html', {'latest_news': latest_news})

@login_required
def token_balance(request):
    # İstifadəçinin token balansını almaq
    token, created = Token.objects.get_or_create(user=request.user)
    return render(request, 'news/token_balance.html', {'token': token})