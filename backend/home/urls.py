from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from home.views import BlogView, PublicBlogView

router = routers.DefaultRouter()
router.register(r"posts", PublicBlogView)

urlpatterns = [
    path("", include(router.urls)),
    path("blog/", BlogView.as_view()),
]