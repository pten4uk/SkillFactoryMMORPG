from django.urls import reverse
from django.views.generic import ListView, CreateView

from .forms import PostCreateForm
from .models import Post


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'


class PostCreate(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'newsboard/post_create.html'

    def get_success_url(self):
        return reverse('newsboard:home')



