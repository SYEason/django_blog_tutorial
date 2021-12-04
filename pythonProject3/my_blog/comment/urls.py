from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
    path('comment-del/<int:id>/', views.comment_del, name='comment_del'),

]