from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class HomePageUpdateModel(models.Model):
    title = models.CharField(max_length=255)  # 更新されたコンテンツのタイトル
    content = models.TextField()  # 更新されたコンテンツの本文

    # 更新者や日時
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # 更新を行ったユーザー
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.updated_at}"



