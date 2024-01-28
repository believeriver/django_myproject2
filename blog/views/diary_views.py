from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
from blog.models import DiaryModel


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'pages/diary_list.html'
    model = DiaryModel
    paginate_by = 30

    def get_queryset(self):
        queryset = DiaryModel.objects.order_by('-diary_date')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(jp_text__icontains=keyword) | Q(diary_date__icontains=keyword)
            )
        return queryset


class DetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'pages/diary_detail.html'
    model = DiaryModel


class CreateView(LoginRequiredMixin, generic.CreateView):
    """ログインを強制:LoginRequiredMixin"""
    template_name = 'pages/diary_create.html'
    model = DiaryModel
    fields =('title','diary_date','jp_text', 'en_text','created_at')
    success_url = reverse_lazy('blog:diary_index')


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'pages/diary_update.html'
    model = DiaryModel
    fields =('title','diary_date','jp_text', 'en_text')
    success_url = reverse_lazy('blog:diary_index')


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'pages/diary_delete.html'
    model = DiaryModel
    success_url = reverse_lazy('blog:diary_index')