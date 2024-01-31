from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # ユーザーとの一対一のリレーション
    name = models.CharField(default='', blank=True, max_length=50)
    bio = MarkdownxField(blank=True, null=True)  # プロフィールの自己紹介文
    hobby = MarkdownxField(blank=True, null=True)  # 趣味
    work_experience = MarkdownxField(blank=True, null=True)  # 業務経験
    qualifications = MarkdownxField(blank=True, null=True)  # プロフィールの自己紹介文
    location = models.CharField(max_length=255, blank=True, null=True)  # 住所や場所など
    birthdate = models.DateField(blank=True, null=True)  # 誕生日
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # プロフィール画像
    contact_email = models.EmailField(blank=True, null=True)  # 連絡先メールアドレスなど
    tel = models.CharField(default='', blank=True, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def convert_bio_markdown_to_html(self):
        return markdownify(self.bio)

    def convert_hobby_markdown_to_html(self):
        return markdownify(self.hobby)

    def convert_work_experience_markdown_to_html(self):
        return markdownify(self.work_experience)

    def convert_qualifications_markdown_to_html(self):
        return markdownify(self.qualifications)

    def __str__(self):
        return self.name

