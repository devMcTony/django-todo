from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.todos, name="home"),
    path("", views.todos, name="Todos"),
    path("about", views.about, name="About"),
    path("edit/<int:todo_id>", views.edit, name="edit"),
]