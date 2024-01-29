from django.urls import path

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from blog import views

app_name = 'blog'

urlpatterns = [
    path('login/', views.login_func, name='login'),
    path('logout/', views.logout_func, name='logout'),
    path('liked/<int:pk>/', views.liked_func, name='liked'),
    path('status_open/<int:pk>/', views.status_open, name='status_open'),
    path('status_hidden/<int:pk>/', views.status_hidden, name='status_hidden'),
    path('comment/<int:post_pk>/', views.PostCommentView.as_view(), name='comment'),
    path('about/', views.AboutMe.as_view(), name='about'),
    path('', views.CoverView.as_view(), name='cover'),
]

post_org_urlpatterns = [
    path('blog/', views.PostIndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('category/<int:pk>/', views.PostCategoryView.as_view(), name='category'),
]

post_mark_urlpatterns = [
    path('blog_mark/', views.PostIndexMarkView.as_view(), name='index_mark'),
    path('detail_mark/<int:pk>/', views.PostDetailMarkView.as_view(), name='detail_mark'),
    path('update_mark/<int:pk>/', views.PostUpdateMarkView.as_view(), name='update_mark'),
    path('create_mark/', views.PostCreateMarkView.as_view(), name='create_mark'),
    path('delete_mark/<int:pk>/', views.PostDeleteMarkView.as_view(), name='delete_mark'),
    path('category_mark/<int:pk>/', views.PostCategoryMarkView.as_view(), name='category_mark'),
]

todo_urlpatterns = [
    path('todo_list/', views.TodoList.as_view(), name='todo_list'),
    path('todo_detail/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'),
    path('todo_create/', views.TodoCreate.as_view(), name='todo_create'),
    path('todo_delete/<int:pk>', views.TodoDelete.as_view(), name='todo_delete'),
    path('todo_update/<int:pk>', views.TodoUpdate.as_view(), name='todo_update'),
]

diary_urlpatterns = [
    path('diary_list/', views.IndexView.as_view(), name='diary_index'),
    path('diary_detail/<int:pk>', views.DetailView.as_view(), name='diary_detail'),
    path('diary_create/', views.CreateView.as_view(), name='diary_create'),
    path('diary_delete/<int:pk>', views.DeleteView.as_view(), name='diary_delete'),
    path('diary_update/<int:pk>', views.UpdateView.as_view(), name='diary_update'),
]

homepage_update_urlpatterns = [
    path('home/', views.HomeIndexView.as_view(), name='home'),
]

urlpatterns += post_org_urlpatterns
urlpatterns += post_mark_urlpatterns
urlpatterns += todo_urlpatterns
urlpatterns += diary_urlpatterns
urlpatterns += homepage_update_urlpatterns




