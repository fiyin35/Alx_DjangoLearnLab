from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView

from .forms import CustomUserCreationForm, CommentForm, PostForm


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
        context_object_name = 'post'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["comments"] = self.object.comments.all()  # Load comments related to the post
                context["form"] = CommentForm()  # Initialize comment form
                return context
class PostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
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
                form = UserChangeForm(request.POST, instance=request.user)
                if form.is_valid():
                        form.save()
                        return redirect('profile')
        else:
                form = UserChangeForm(instance=request.user)
        return render(request, 'blog/profile.html', {'form': form})


# comments views go here
@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_add.html', {'form': form})

@login_required
def CommentUpdateView(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form})


@login_required
def CommentDeleteView(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=comment.post.id)
    return render(request, 'blog/comment_delete.html', {'comment': comment})

# class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
#         model = Comment
#         form_class = CommentForm
#         template_name = 'blog/post_detail.html'

#         def test_func(self):
#                 comment = self.get_object()
#                 return self.request.user == comment.author

# class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
#         model = Comment
#         template_name = 'blog/post_detail.html'

#         def test_func(self):
#                 comment = self.get_object()
#                 return self.request.user == comment.author

# class CommentViewAll(ListView, LoginRequiredMixin):
#         #referencing the Comment in model
#         model = Comment
#         # path to the html template
#         template_name = 'blog/post_detail.html'
#         # rename the object name, usable in the html template
#         context_object_name = 'comments'
#         # order by latest post
#         ordering = ['-created_at']
