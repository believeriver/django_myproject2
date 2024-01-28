from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import Http404

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from blog.models import Post, Category, Comment
from .forms import CommentCreateForm


def signup_func(request):
    """create new user"""
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'pages/signup.html', {'error': 'このユーザは登録されています'})
        except:
            # user = User.objects.create_user(username2, '', password2)
            return render(request, 'pages/login.html', {'some': 100})
    return render(request, 'pages/signup.html', {'some': 100})


def login_func(request):
    """ login user """
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            return redirect('blog:login')
    return render(request, 'pages/login.html')


def logout_func(request):
    """logout user"""
    logout(request)
    return redirect('blog:login')


def liked_func(request, pk):
    post = Post.objects.get(pk=pk)
    post.liked = post.liked + 1
    post.save()
    return redirect('blog:index_mark')


def status_open(request, pk):
    post = Post.objects.get(pk=pk)
    post.status = 2
    post.save()
    return redirect('blog:index_mark')


def status_hidden(request, pk):
    post = Post.objects.get(pk=pk)
    post.status = 1
    post.save()
    return redirect('blog:index_mark')


class AboutMe(generic.TemplateView):
    template_name = 'pages/main_about_me.html'


class HomeView(generic.TemplateView):
    template_name = 'pages/main_home.html'


class CoverView(generic.TemplateView):
    template_name = 'pages/main_cover.html'


class PostCommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        # コメントはまだDBに保存されていない
        comment = form.save(commit=False)
        # ポストとの紐付けを内部で行う
        comment.post = get_object_or_404(Post, pk=post_pk)
        # ここでDBに保存
        comment.save()
        return redirect('blog:detail', pk=post_pk)


class PostCategoryView(generic.ListView):
    template_name = 'pages/post_list.html'
    model = Post
    paginate_by = 10

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk)

        return queryset


class PostIndexView(generic.ListView):
    template_name = 'pages/post_list.html'
    model = Post
    paginate_by = 7

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


class PostDetailView(generic.DetailView):
    template_name = 'pages/post_detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    """ログインを強制するには、先にLoginRequiredMixinを記入（継承）する必要があるみたい"""
    template_name = 'pages/post_create.html'
    model = Post
    fields = ('title', 'text', 'codememo', 'created_at', 'category')
    success_url = reverse_lazy('blog:index')


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'pages/post_update.html'
    model = Post
    fields = ('title', 'text', 'codememo', 'created_at', 'category')
    success_url = reverse_lazy('blog:index')


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'pages/post_delete.html'
    model = Post
    success_url = reverse_lazy('blog:index')


"""
2024.1.20
for markdown field.
"""


class PostIndexMarkView(generic.ListView):
    template_name = 'pages/post_mark_list.html'
    model = Post
    paginate_by = 7

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')

        if self.request.user.is_authenticated and self.request.user.is_staff:
            """認証されかつStaff(管理者権限）の時は全て表示"""
            queryset = queryset.filter(
                Q(status__icontains=1) | Q(status__icontains=2)
            )
        else:
            """一般公開のみを表示"""
            queryset = queryset.filter(Q(status__icontains=2))

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(content__icontains=keyword)
            )
        return queryset


class PostDetailMarkView(generic.DetailView):
    model = Post
    template_name = 'pages/post_mark_detail.html'


class PostCreateMarkView(LoginRequiredMixin, generic.CreateView):
    template_name = 'pages/post_mark_create.html'
    model = Post
    fields = ('title', 'content', 'created_at', 'category')
    success_url = reverse_lazy('blog:index_mark')


class PostUpdateMarkView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'pages/post_mark_update.html'
    model = Post
    fields = ('title', 'content', 'created_at', 'category')
    success_url = reverse_lazy('blog:index_mark')


class PostDeleteMarkView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'pages/post_delete.html'
    model = Post
    success_url = reverse_lazy('blog:index_mark')


class PostCategoryMarkView(generic.ListView):
    template_name = 'pages/post_mark_list.html'
    model = Post
    # paginate_by = 10

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk)

        return queryset





