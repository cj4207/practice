from django.urls import path
from .views import SampleOwnerView, SampleDogView

urlpatterns = [
    path('/owner', SampleOwnerView.as_view()),
    path('/dog', SampleDogView.as_view())
]
