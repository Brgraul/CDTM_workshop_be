from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import PostForm
from .models import Post
from .forms import PostForm
from datetime import datetime

# This function displays the content of index.html
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


def new_post(request):
    # If the method is POST, we retrieve the form and save it to the DB
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date_posted = datetime.now()
            post.save()
            return redirect("index")
    # Otherwise we just load the page
    else:
        form = PostForm()
    return render(request, "newpost.html", {"form": form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm()
    return HttpResponseRedirect("/")


# This function returns a generic response
def requestHandle(request):
    # Actions to be made when a request is received
    return HttpResponse("This is dummy code")
