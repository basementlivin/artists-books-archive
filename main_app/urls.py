from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('books/', views.BookList.as_view(), name="book_list"),
    path('books/new/', views.BookCreate.as_view(), name="book_create"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    path('publishers/', views.PublisherList.as_view(), name="publisher_list"),
]