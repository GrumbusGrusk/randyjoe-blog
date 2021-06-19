from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Music
from blog.forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import CommentForm
from .filters import OrderFilter
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def base(request):
    return render(request, 'blog/base.html',)

def dashboard(request):
    return render(request, "blog/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(request, "blog/register.html",{"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def music(request):
    musics = Music.objects.all()
    myFilter = OrderFilter(request.GET, queryset=musics)
    musics = myFilter.qs
    return render(request, 'blog/music.html', {'musics': musics, 'myFilter':myFilter})
