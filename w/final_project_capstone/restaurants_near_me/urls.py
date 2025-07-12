from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("near_me", views.page, name="near_me"),
    path("<str:id>", views.restaurant, name="restaurant"),
    path("like/", views.like, name="like"),
    path("delete/", views.delete, name="delete")
]
