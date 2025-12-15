from django.shortcuts import render, redirect
from .models import Author, Post, Comment
from .forms import AuthorForm, PostForm, CommentForm, PostSearchForm

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_author')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_post')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_comment')
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})

def search_post(request):
    form = PostSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        title = form.cleaned_data.get('title')
        results = Post.objects.filter(title__icontains=title)
    return render(request, 'search_post.html', {'form': form, 'results': results})