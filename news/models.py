from django.db import models
from django.contrib.auth.models import User  # İstifadəçiləri izləmək üçün
from django.utils import timezone
from PIL import Image
import os

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Şəkil saxlanmadan əvvəl ölçüləri dəyişdiririk
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')  # Şəkli RGB formatına çeviririk
            img.thumbnail((400, 400))  # 400x400 ölçüsündə sıxılmasını təmin edirik (kəsmədən)
            img.save(self.image.path)  # Şəkli yenidən saxlayırıq

        super().save(*args, **kwargs)  # Dəyişiklikləri saxlayırıq

    def __str__(self):
        return self.title

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # İstifadəçi ilə əlaqələndirmək
    balance = models.PositiveIntegerField(default=0)  # İstifadəçinin balansı
    last_updated = models.DateTimeField(auto_now=True)  # Token balansının sonuncu dəfə yenilənmə tarixi

    def add_tokens(self, amount):
        """İstifadəçiyə token əlavə etmək"""
        self.balance += amount
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.balance} Tokens"