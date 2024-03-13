from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.models import User


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()
    context = {'post': post, 'comments': comments}
    if request.user.is_authenticated:
        form = CreateCommentForm()
        if request.method == 'POST':
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                user_id = int(request.user.id)
                comment.author = User.objects.get(id=user_id)
                comment.post = Post.objects.get(id=post_id)
                comment.save()
                return redirect('posts', post_id=post_id)
        context["form"] = form
    return render(request, 'post.html', context)


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user_id = int(request.user.id)
            post.author = User.objects.get(id=user_id)
            post.save()
            return redirect('home')
    else:
        form = CreatePostForm()
    context = {'form': form}
    return render(request, 'create_post.html', context)
