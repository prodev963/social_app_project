from ctypes import resize
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class PostListView(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'post')


class UserPostsListView(generic.ListView):
    model = models.Post
    template_name: str = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(
                username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetailView(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        return super().get_queryset().filter(user__username__iexact = self.kwargs.get('username'))        

class PostCreateView(LoginRequiredMixin,SelectRelatedMixin, generic.CreateView):
    fields = ('message' , 'group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        return super().get_queryset().filter(user_id = self.request.user.id)

    def delete(self, request, *args, **kwargs):
        # messages.success(self.request, 'post deleted')
        return super().delete(request, *args, **kwargs)            