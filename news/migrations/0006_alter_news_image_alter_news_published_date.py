# Generated by Django 4.2.18 on 2025-02-01 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_id_alter_news_published_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
