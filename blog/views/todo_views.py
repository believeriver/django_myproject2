from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from blog.models import TodoModel


class TodoList(LoginRequiredMixin, ListView):
    template_name = 'pages/todo_list.html'
    model = TodoModel
    paginate_by = 15

    def get_queryset(self):
        queryset = TodoModel.objects.order_by('-duedate')
        keyword = self.request.GET.get('keyword')
        if keyword:
            if keyword == 'high':
                keyword = 'danger'
            elif keyword == 'normal':
                keyword = 'info'
            elif keyword == 'low':
                keyword = 'success'
            elif keyword == 'finish':
                keyword = 'secondary'

            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(memo__icontains=keyword) | Q(priority__icontains=keyword)
            )
        return queryset


class TodoDetail(LoginRequiredMixin, DetailView):
    template_name = 'pages/todo_detail.html'
    model = TodoModel


class TodoCreate(LoginRequiredMixin, CreateView):
    template_name = 'pages/todo_create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('blog:todo_list')


class TodoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'pages/todo_delete.html'
    model = TodoModel
    success_url = reverse_lazy('blog:todo_list')


class TodoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'pages/todo_update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('blog:todo_list')
