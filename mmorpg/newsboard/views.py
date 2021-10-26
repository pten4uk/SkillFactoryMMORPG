from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .forms import PostCreateForm
from .models import *


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-datetime_of_last_update')


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'newsboard/post_create.html'

    def get_success_url(self):
        return reverse('newsboard:home')

    def form_valid(self, form):
        post = form.save(commit=False)
        user = self.request.user
        post.author = user
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'newsboard/post_create.html'

    def get_success_url(self):
        return reverse('newsboard:home')

    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно обновлена!')
        return super().form_valid(form)


class CommentsList(ListView):
    model = Comment
    template_name = 'newsboard/post_comments.html'
    ordering = ('-datetime_of_creation')