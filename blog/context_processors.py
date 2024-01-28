import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
from .models import Category
from django.db.models import Count, Q


def common(request):
    """テンプレートに毎回渡すデータ"""
    context = {
        'category_list': Category.objects.all(),
        'categories': Category.objects.annotate(
            count=Count("post", Q(post__status=2))
        )
    }
    # # check print
    # for category in context['categories']:
    #     print(vars(category))
    return context