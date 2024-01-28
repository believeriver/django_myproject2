from django.db import models
from django.utils import timezone


# Diary model
class DiaryModel(models.Model):
    """日記データベース"""
    title = models.CharField('タイトル', max_length=255)
    diary_date = models.DateTimeField('日記日付', default=timezone.now)
    jp_text = models.TextField('本文')
    en_text = models.TextField('英語日記', blank=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title