from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name = "title"),
    path("search", views.search, name = "search"),
    path("wiki/edit/<str:name>", views.edit, name = "edit"),
    path("new", views.new, name = "new"),
    path("random", views.random, name = "random")
]