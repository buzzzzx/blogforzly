from django.shortcuts import render, get_object_or_404, redirect

from .models import Comment
from .forms import CommentForm
from blog.models import Post
from utils.send_email import send


# Create your views here.

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # comment.text = form.text
            comment.save()

            # send email
            send(flag=1, nickname=comment.name, semail=comment.email, text=comment.text, postname=comment.post.title)

            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
