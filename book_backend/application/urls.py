from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('HowToStopWorryingAndStartLiving/', BookRepo, name='book_repo'),
]