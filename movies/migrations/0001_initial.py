# Generated by Django 3.2.3 on 2021-05-27 01:23

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
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=200)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField()),
                ('adult', models.BooleanField()),
                ('budget', models.CharField(max_length=20)),
                ('poster_path', models.CharField(max_length=500)),
                ('release_date', models.DateField()),
                ('runtime', models.CharField(max_length=5)),
                ('vote_average', models.CharField(max_length=5)),
                ('video', models.CharField(max_length=500)),
                ('backdrop_path', models.CharField(max_length=500)),
                ('movie_vote', models.FloatField(default=0)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_vote', models.IntegerField()),
                ('content', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
