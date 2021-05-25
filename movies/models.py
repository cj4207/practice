from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    runnig_time = models.IntegerField()
    actor = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'movies'

'''class Actor_Movie(models.Model):
    actor = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'actors_movies'''''