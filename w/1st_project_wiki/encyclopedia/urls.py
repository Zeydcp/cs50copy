from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry, name="wiki_entry"),
    path("search/", views.search, name="wiki_search"),
    path("create/", views.create, name="create_page"),
    path("edit/<str:name>", views.edit, name="edit_page"),
    path("random/", views.random_entry, name="random")
]
