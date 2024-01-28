from django.db import models
from django.utils import timezone

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    ブログの記事
    2024.1.20 add Markdown flied. text filed is changed to accept default none
    """
    title = models.CharField('タイトル', max_length=255)
    content = MarkdownxField(verbose_name='コンテンツ', default=None, null=True, blank=True)
    text = models.TextField('本文', default=None, null=True, blank=True)
    codememo = models.TextField('サンプルコード', blank=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0)
    status = models.PositiveSmallIntegerField(default=1, verbose_name="公開ステータス", help_text="1:非公開, 2:公開")
    liked = models.IntegerField(default=0, verbose_name="いいね数")

    def convert_markdown_to_html(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ブログのコメント"""
    name = models.CharField('お名前', max_length=30, default='名無し')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, verbose_name='紐づく記事', on_delete=models.PROTECT)
    create_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
