from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm, Textarea
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Post, Like, Comment, Follow


class NewPostingForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']

        widgets = {
            'body': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Post',
                'rows': 2
            })
        }


class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Comment',
            })
        }


def like(request):
    try:
        data = loads(request.body)
        post = get_object_or_404(Post, id=int(data.get("id")))
    except:
        return None

    if not request.user.is_authenticated:
        return JsonResponse({"message": "User not signed in"}, status=401)

    try:
        like = get_object_or_404(Like, liker=request.user, post=post)
    except:
        like = Like(
            liker=request.user,
            post=post
        )
        like.save()
        return JsonResponse({"like": True, "count": post.like_count()}, status=201)
    else:
        like.delete()
        return JsonResponse({"like": False, "count": post.like_count()}, status=201)


def edit(request):
    data = loads(request.body)

    if data.get("id") is not None:
        post = get_object_or_404(Post, id=int(data.get("id")))

        if request.user == post.posted_by:
            post.body = data["body"]
            post.save()
            return JsonResponse({"timestamp": post.timestamp}, status=201)


@csrf_exempt
def index(request):
    posts = Post.objects.order_by('-timestamp')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":

        if (like_return := like(request)) is not None:
            return like_return

        form = NewPostingForm(request.POST)
        # Make sure data is valid
        if form.is_valid():
            posting = form.save(commit=False)
            posting.posted_by = request.user
            posting.save()
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "network/index.html", {
                "form": form,
                "posts": page_obj
            })

    elif request.method == "PUT":
        return edit(request)
    else:
        return render(request, "network/index.html", {
            "form": NewPostingForm(),
            "posts": page_obj
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
def profile(request, user):
    user_ = get_object_or_404(User, username=user)
    posts = user_.posts.order_by('-timestamp')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "posts": page_obj,
        "user_": user_,
        "num_posts": posts.count()
    }

    if request.user.is_authenticated:
        following = Follow.objects.filter(user_1=request.user, user_2=user_).exists()
        context["following"] = following

    if request.method == "POST":
        data = loads(request.body)
        type = data.get("type")

        if type == "follow":
            try:
                follow = get_object_or_404(Follow, user_1=request.user, user_2=user_)
            except:
                follow = Follow(
                    user_1=request.user,
                    user_2=user_
                )
                follow.save()
                return JsonResponse({"follow": True, "count": user_.follower_count()}, status=201)
            else:
                follow.delete()
                return JsonResponse({"follow": False, "count": user_.follower_count()}, status=201)
        else:
            return like(request)

    elif request.method == "PUT":
        return edit(request)

    else:
        return render(request, "network/page.html", context)


@csrf_exempt
def following(request):

    posts = Post.objects.filter(posted_by__in=request.user.follows.values_list(
        'user_2', flat=True)).order_by('-timestamp')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        return like(request)

    context = {
        "posts": page_obj
    }
    return render(request, "network/following.html", context)
