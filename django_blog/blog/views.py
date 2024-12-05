from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView

from .forms import CustomUserCreationForm


# Create your views here.
class Registration(CreateView):
        form_class = CustomUserCreationForm
        template_name = 'blog/register.html'
        # redirect the user to login url after succesful login
        success_url = reverse_lazy('login')
class PostListView(ListView):
        #referencing the post in model
        model = Post
        # path to the html template
        template_name = 'blog/post_list.html'
        # rename the object name, usable in the html template
        context_object_name = 'posts'
        # order by latest post
        ordering = ['-created_at']
class PostDetailView(DetailView, LoginRequiredMixin):
        model = Post
        template_name = 'blog/post_detail.html'
class PostCreateView(CreateView, LoginRequiredMixin):
        model = Post
        form_class = PostForm
        template_name = 'blog/post_create.html'

        def form_valid(self, form):
                # automatically set post author to login user
                form.instance.author = self.request.user
                return super().form_valid(form)
        
# update view - author can update post
class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
        model = Post
        form_class = PostForm
        template_name = 'blog/post_update.html'

        def test_func(self):
                post = self.get_object()
                return self.request.user == post.author # ensure only author can update


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
        model = Post
        template_name = 'blog/post_delete.html'
        success_url = reverse_lazy('blog:post_list') 

        def test_func(self):
                post = self.get_object()
                return self.request.user == post.author

@login_required
def profile(request):
        if request.method == 'POST':
                form = UserChangeForm(request.POST, intance=request.user)
                if form.is_valid():
                        form.save()
                        return redirect('profile')
        else:
                form = UserChangeForm(instance=request.user)
        return render(request, 'blog/profile.html', {'form': form})



