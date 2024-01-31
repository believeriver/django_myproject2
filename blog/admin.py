from django.contrib import admin
from .models import (
    Post,
    Category,
    Comment,
    TodoModel,
    DiaryModel,
    HomePageUpdateModel,
    Profile,
)
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(TodoModel)
admin.site.register(DiaryModel)
admin.site.register(HomePageUpdateModel)
admin.site.register(Profile)
admin.site.unregister(Group)

