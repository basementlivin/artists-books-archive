from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Book
from django.views.generic import DetailView


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class BookList(TemplateView):
    template_name = "books.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["books"] = Book.objects.filter(title__icontains=title)
            context["header"] = f"Results for '{title}'"
        else:
            context["books"] = Book.objects.all()
            context["header"] = "Recent additions"
        return context

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'artist', 'publisher', 'release_year', 'description', 'image']
    template_name = "book_create.html"
    success_url = "/books/"

class BookDetail(DetailView):
    model = Book
    template_name = "book_create.html"

class PublisherList(TemplateView):
    template_name = "publishers.html"