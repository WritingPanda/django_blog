from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def posts_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 3)
    page_request_var = "page"
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "List",
        "obj_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, 'posts/post_list.html', context=context)


def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Create",
        "form": form,
    }
    return render(request, 'posts/post_form.html', context=context)


def posts_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, 'posts/post_detail.html', context=context)


def posts_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully edited!")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, 'posts/post_update.html', context=context)


def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted!")
    return redirect("posts:list")
