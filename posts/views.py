from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "obj_list": queryset
    }
    return render(request, 'posts/index.html', context=context)


def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "title": "Create",
        "form": form
    }
    return render(request, 'posts/post_form.html', context=context)


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'posts/post_detail.html', context=context)


def posts_update(request):
    context = {
        "title": "Update"
    }
    return render(request, 'posts/index.html', context=context)


def posts_delete(request):
    context = {
        "title": "Delete"
    }
    return render(request, 'posts/index.html', context=context)
