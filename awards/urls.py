from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home_page, name = 'home_page'),
    path("project/post/", views.post, name = "post"),
    path("profile/", views.user_profile, name = 'profile'),
    path("project/<int:project_id>/", views.project_detail, name = "details"),
    path("search/projects/results/", views.search, name = "search"),
    path("logout/", views.logout, name = "logout"),
]