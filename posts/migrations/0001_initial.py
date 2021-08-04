# Generated by Django 3.2.5 on 2021-07-16 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('plus', models.SmallIntegerField(verbose_name='За')),
                ('minus', models.SmallIntegerField(verbose_name='Против')),
                ('local', models.CharField(max_length=20)),
                ('shop', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='price')),
                ('currency', models.CharField(max_length=100, verbose_name='Валюта')),
                ('comment_count', models.SmallIntegerField(verbose_name='Количество комментариев')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaFile', models.FileField(upload_to='')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]