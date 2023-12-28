from django.views.generic import ListView, DetailView, DeleteView
from .models import Post
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# выводим содержимое нашей модели базы данных
class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"


class BlogUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "body",
    )
    template_name = "post_edit.html"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = (
        "title",
        "body",
        "author"
    )