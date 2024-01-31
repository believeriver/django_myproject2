from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
from blog.models import Profile


OWNER_NAME = 'nono'


class ProfileIndexView(generic.View):
    template_name = 'pages/main_about_me.html'
    # model = Profile

    def get(self, request, *args, **kwargs):
        # ユーザー名に基づいてプロフィールオブジェクトを取得
        # username = kwargs.get('username')
        username = OWNER_NAME
        profile = Profile.objects.get(user__username=username)

        # テンプレートにデータを渡す
        context = {'profile': profile}

        # テンプレートをレンダリングしてレスポンスを返す
        return render(request, self.template_name, context)
