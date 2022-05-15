# coding: utf-8

from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class GetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'making_time', 'serves', 'ingredients', 'cost']