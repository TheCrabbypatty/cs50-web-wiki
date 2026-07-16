from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.pages, name="pages"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name = "random"),
    path("new_page", views.new_page, name = "new_page"),
    path("wiki/edit/<str:page>", views.edit_page, name = "edit_page")
]
