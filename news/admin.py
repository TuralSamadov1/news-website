from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'category', 'summary', 'image')
    search_fields = ('title', 'content', 'category')
    list_filter = ('published_date', 'category')

admin.site.register(News, NewsAdmin)
