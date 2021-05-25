from django.urls import path
from .views import MovieView, ActorView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', ActorView.as_view())
]