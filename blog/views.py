from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.http import HttpResponseNotFound
from .forms import PostShareForm, CommentForm
from django.core.mail import send_mail
# Create your views here.
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request, tag_slug=None):

    posts = Post.published.all()
    tag = None

    if tag_slug:
        tag = Tag.objects.filter(slug=tag_slug)
        if tag:
            posts = Post.published.filter(tags__in=tag)
            tag = tag[0]
        else:
            return HttpResponseNotFound(f"<h1>There is no posts with {quote(tag_slug)} slug!</h1>")

    paginator = Paginator(posts, 5, orphans=3)
    page = request.GET.get("page", 1)
    posts = paginator.page(page)

    context = {
        'posts': posts,
        'tag': tag,
        'selected': 'blog'
    }
    return render(
        request,
        'blog/list.html',
        context
    )


@login_required
def post_detail(request, year, month, day, post):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )

    comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form
    }

    return render(
        request,
        'blog/detail.html',
        context
    )


@login_required
def post_share(request, post_slug):
    post = get_object_or_404(
        Post,
        slug=post_slug,
        status=Post.Status.PUBLISHED
    )

    shared = False

    if request.method == "POST":
        form = PostShareForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            # building absolute url for post
            post_url = request.build_absolute_uri(post.get_absolute_url())

            sender_name = cd.get('name')
            sender_email = cd.get('email')
            recipient = cd.get('recipient')
            comment = cd.get('comment')

            subject = (
                f"{sender_name}({sender_email})"
                f"شما را به خواندن پست '{post.title}' دعوت میکند"
            )

            message = (
                f"جهت مطالعه ی این پست وارد لینک زیر شوید\n"
                f"{post_url}\n\n"
                f"توضیحات فرستنده:{comment}"
            )
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=None,
                    recipient_list=[recipient]
                )
                shared = True
            except Exception as e:
                print(e)
    else:
        form = PostShareForm()
    context = {
        "form": form,
        "shared": shared
    }
    return render(
        request,
        'blog/post_share.html',
        context
    )


@login_required
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    comment = None

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {
        'post': post,
        'form': form,
        'comment': comment
    }

    return render(
        request,
        'blog/post_comment.html',
        context
    )
