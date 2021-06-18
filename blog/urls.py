from django.urls import path
from . import views
from django.conf.urls import include, url
from blog.views import register

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name='dashboard'),
    url(r"^blog/", views.post_list, name='blog'),
    url(r"^register/", register, name="register"),
    url(r"^music/", views.music, name='music'),
]
