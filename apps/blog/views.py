import markdown

from django.shortcuts import render, get_object_or_404
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Post, Category, Tag, Contact
from comments.forms import CommentForm
from .forms import ContactForm
from utils.send_email import send


# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')

    # page
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, 5, request=request)

    posts = p.page(page)

    return render(request, 'blog/index.html', context={'post_list': posts})


def blog_list(request):
    post_list = Post.objects.all().order_by('-created_time')

    # page
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, 5, request=request)

    posts = p.page(page)

    return render(request, 'blog/full-width.html', context={'post_list': posts})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    msg = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ct = form.save()
            # send email
            send(flag=2, nickname=ct.name, semail=ct.email, text=ct.message)
            msg = 'Success'
            form.clean()
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form, 'msg': msg})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    post.increase_views()

    # Markdown codehilite语法高亮，toc生成目录
    # post.body = markdown.markdown(
    #     post.body,
    #     extensions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #         'markdown.extensions.toc',
    #     ]
    # )
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }

    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    # page
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, 7, request=request)

    posts = p.page(page)
    return render(request, 'blog/index.html', context={'post_list': posts})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, 7, request=request)

    posts = p.page(page)
    return render(request, 'blog/index.html', context={'post_list': posts})


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=tag).order_by('-created_time')
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, 7, request=request)

    posts = p.page(page)
    return render(request, 'blog/index.html', context={'post_list': posts})
