# Generated by Django 5.2.1 on 2025-06-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('directors_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='movie')),
                ('watch_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
