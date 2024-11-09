# Generated by Django 5.1.1 on 2024-10-16 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='blog_app.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Фото поста',
                'verbose_name_plural': 'Фото поста',
            },
        ),
    ]