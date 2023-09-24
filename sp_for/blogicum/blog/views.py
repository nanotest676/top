from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


POST_COUNT = 5


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category',
        'author'
    ).prefetch_related('location').filter(
        pub_date__lte=datetime.now(),
        is_published__exact=True,
        category__is_published=True
    )[:POST_COUNT]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    time_now = timezone.now()
    post_detail = get_object_or_404(
        Post.objects.select_related('category')
        .prefetch_related(
            'location'
        ).filter(
            pub_date__lte=time_now,
            is_published=True,
            category__is_published=True
        ), id=id
    )
    context = {'post': post_detail}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    time_now = timezone.now()
    post_category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_list = Post.objects.filter(
        is_published=True,
        category__exact=post_category,
        pub_date__lte=time_now,
        category=post_category
    )
    context = {
        'category': post_category,
        'post_list': post_list
    }
    return render(request, template, context)
