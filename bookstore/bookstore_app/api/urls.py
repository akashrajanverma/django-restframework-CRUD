from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('add_user', views.add_user),
]