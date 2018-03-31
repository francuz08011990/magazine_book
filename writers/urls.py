from django.urls import path

from . import views


app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:author_id>/books/', views.books, name='shell'),
]
