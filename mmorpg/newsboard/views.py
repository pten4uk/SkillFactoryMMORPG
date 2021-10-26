from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
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


class CommentsList(View):
    def get(self, request, *args, **kwargs):
        post_pk = kwargs['post_pk']
        post = Post.objects.get(pk=post_pk)
        qs = Comment.objects.filter(post=post)
        print(qs)
        context = {
            'comments': qs,
            'post': post
        }
        return render(request, 'newsboard/post_comments.html', context)
