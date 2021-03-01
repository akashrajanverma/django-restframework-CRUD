from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('add_author', views.add_author),
    path('add_book', views.add_book),
    path('get_all_books', views.get_all_books),
    path('update_book_title', views.update_book_title)
]