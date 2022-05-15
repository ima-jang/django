# coding: utf-8

from django.urls import path, re_path
from rest_framework import routers
from .views import RecipeViewSet, RecipeRetrieveAPIView, RecipeAllAPIView
from . import views

app_name = 'recipes'
router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('<pk>', views.RecipeRetrieveAPIView.as_view())
]