# app/views.py

from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Post
from .forms import PostForm


def post_list_view(request):
    """
    投稿を一覧表示するview
    """
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PostForm()
        return redirect(reverse('app:list'))
    template_name = 'app/list.html'
    posts = Post.objects.all()
    context = {
        'object_list': posts,
        'form': form,
    }
    return render(request, template_name, context)


def post_detail_view(request, id):
    """
    投稿の詳細を表示するview
    """
    template_name = 'app/detail.html'
    post = get_object_or_404(Post, pk=id)
    context = {
        'object': post,
    }
    return render(request, template_name, context)
