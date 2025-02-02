# news_website/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # news tətbiqinin URL-ləri
    path('', include('news.urls')),  # Home page üçün news app-ini əlavə etdik
]

# Media fayllarını idarə etmək üçün Debug rejimində aşağıdakı kodu əlavə edirik
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
