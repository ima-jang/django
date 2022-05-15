from django.shortcuts import render

# coding: utf-8

import django_filters
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .models import Recipe
from .serializer import *



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = GetAllSerializer

    def list(self, request, *args, **kwargs):
        """Recipeをpkで取得"""

        # モデルのオブジェクト取得
        queryset = Recipe.objects.all()

        # シリアライズ
        serializer = RecipeSerializer(instance=queryset, many=True)

        datas = serializer.data
        """it = 1
        for r in datas:
            r["id"] = it
            it += 1
        """
        retval = {"recipes": datas}

        # 返却
        return Response(retval, status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        """Recipeをpkで取得"""

        # モデルのオブジェクト取得
        instance = get_object_or_404(Recipe, pk=pk)

        # シリアライズ
        serializer = RecipeSerializer(instance)

        r = {"message": "Recipe details by id", "recipe": serializer.data}

        # 返却
        return Response(r, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """本モデルの登録APIに対応するハンドラメソッド"""

        # シリアライザオブジュエクトを作成
        serializer = RecipeSerializer(data=request.data)
        # バリデーション
        if serializer.is_valid():
            # モデルオブジェクトを登録
            serializer.save()
            retval =[]
            retval.append(serializer.data)
            # レスポンス
            return Response({'message': "Recipe successfully created!", 'recipe': retval}, status.HTTP_200_OK)  
        else:
            reterr = "title, making_time, serves, ingredients, cost"
            return Response({"message": "Recipe creation failed!", "required!": reterr}, status.HTTP_404_NOT_FOUND)


    def update(self, request, pk, *args, **kwargs):
        """
        パスパラメータのpkを受け取りbodyの地区番号に更新
        """
        # instanceの取得
        instance = get_object_or_404(Recipe, pk=pk)

        # シリアライザの作成
        serializer = GetAllSerializer(instance=instance, data=request.data, partial=True)

        # バリデーション
        serializer.is_valid(raise_exception=True)

        # DB更新
        if serializer.save():
            retval =[]
            serializer.data["id"] = pk
            retval.append(serializer.data)
            # レスポンス
            return Response({'message': "Recipe successfully updated!", 'recipe': retval}, status.HTTP_200_OK) 

        else:
            reterr = "title, making_time, serves, ingredients, cost"
            return Response({"message": "Recipe creation failed!", "required!": reterr}, status.HTTP_404_NOT_FOUND) 

    def destroy(self, request, pk, *args, **kwargs):

        # instanceの取得
        instance = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(instance)
        if serializer.save():
            instance.delete()
            # レスポンス
            return Response({'message': "Recipe successfully removed!"}, status.HTTP_200_OK)       
        else:
            return Response({'message': "No Recipe found"}, status.HTTP_404_NOT_FOUND)  


class RecipeRetrieveAPIView(APIView):

    def get(self, request, pk, *args, **kwargs):
        """Recipeをpkで取得"""

        # モデルのオブジェクト取得
        instance = get_object_or_404(Recipe, pk=pk)

        # シリアライズ
        serializer = GetAllSerializer(instance)

        retval = []
        r = {"message": "Recipe details by id", "recipe": serializer.data}
        retval.append(r)

        # 返却
        return Response(r, status.HTTP_200_OK)


    def patch(self, request, pk, *args, **kwargs):
        """
        パスパラメータのpkを受け取りbodyの地区番号に更新
        """
        # instanceの取得
        instance = get_object_or_404(Recipe, pk=pk)

        # シリアライザの作成
        serializer = GetAllSerializer(instance=instance, data=request.data, partial=True)

        # バリデーション
        serializer.is_valid(raise_exception=True)

        # DB更新
        serializer.save()

        retval =[]
        retval.append(serializer.data)
        # レスポンス
        return Response({'message': "Recipe successfully updated!", 'recipe': retval}, status.HTTP_200_OK)  



class RecipeAllAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """Recipeをpkで取得"""

        # モデルのオブジェクト取得
        queryset = Recipe.objects.all()

        # シリアライズ
        serializer = GetAllSerializer(instance=queryset, many=True)
        retval = {"recipes": serializer.data}

        # 返却
        return Response(retval, status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        # リクエストをシリアライズ
        serializer = RecipeSerializer(data=request.data)

        # リクエストのバリデーション
        serializer.is_valid(raise_exception=True)

        # リソースの新規作成（create）
        serializer.save()

        retval =[]
        retval.append(request.data)
        # レスポンス
        return Response({'message': "Recipe successfully created!", 'recipe': retval})  


"""
class RecipeCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        # リクエストをシリアライズ
        serializer = RecipeSerializer(data=request.data)

        # リクエストのバリデーション
        serializer.is_valid(raise_exception=True)

        # リソースの新規作成（create）
        serializer.save()

        retval =[]
        retval.append(request.data)
        # レスポンス
        return Response({'message': "Recipe successfully created!", recipe: retval})

"""        
