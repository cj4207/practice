from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Actor, Movie
import json
# Create your views here.

class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(first_name=data['first_name'],last_name=data['last_name'],date_of_birth=data['date_of_birth'])
        return JsonResponse({'result':'SUCCESS'},status=200)
    
    def get(self, request):
        actors_info = Actor.objects.all()
        actor_list=[]
        actor_movie=[]
        for actor_info in actors_info:
            actor = {}
            actors_movie = Movie.objects.filter(actor_id=actor_info.id)
            actor_movie = [actor_movie.append(actor_movie) for actor_movie in actors_movie]
            actor['first_name']=actor_info.first_name
            actor['last_name']=actor_info.last_name
            actor['date_of_birth']=actor_info.date_of_birth
            actor['movies']=actor_movie
            actor_list.append(actor)
        return JsonResponse({'result':actor_list},status=200)

class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        actors = Actor.objects.get(first_name=data['first_name'],last_name=data['last_name'])
        Movie.objects.create(title=data['title'],release_date=data['release_date'],running_time=data['running_time'],actor=actors)
        return JsonResponse({'result':'SUCCESS'},status=200)
    
    def get(self, request):
        movies = Movie.objects.all()
        movies_list=[]
        for movie in movies:
            movie = {}
            movie_actors = Actor.objects.filter(actor_id=movie.actor_id)
            actor_list = [movies_list.append(movie_actor) for movie_actor in movie_actors]
            movie['title']=movie_actors.title
            movie['release_date']=movie_actors.release_date
            movie['running_time']=movie_actors.running_time
            movie['actors']=actor_list
            movies_list.append(movie)
        return JsonResponse({'result':movies_list},status=200)
