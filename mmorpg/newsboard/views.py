from django.views.generic import ListView, CreateView

from .models import Post


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'


class PostCreate(CreateView):
    model = Post
    template_name = 'newspaper/post_create.html'



