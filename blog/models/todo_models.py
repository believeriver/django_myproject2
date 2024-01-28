from django.db import models
from django.utils import timezone


PRIORITY = (('danger', 'high'),
            ('info', 'normal'),
            ('success', 'low'),
            ('secondary', 'finish'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    duedate = models.DateField('期限', default=timezone.now)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

