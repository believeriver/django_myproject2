from django.contrib import admin
from .models import Post, Category, Comment, TodoModel, DiaryModel
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(TodoModel)
admin.site.register(DiaryModel)
admin.site.unregister(Group)
