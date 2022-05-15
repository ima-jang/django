from django.db import models


class Recipe(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=100)
    making_time = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)  
    cost = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)