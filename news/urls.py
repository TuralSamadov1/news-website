from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page üçün index view
    path('detail/<int:id>/', views.news_detail, name='news_detail'),
]