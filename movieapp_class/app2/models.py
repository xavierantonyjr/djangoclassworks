from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    directors_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to='movie', null=True, blank=True)
    watch_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.movie_name
