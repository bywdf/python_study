# 定义learning_logs的URL模式

# from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    #主页
    # url('^$', views.index, name = 'index' ),
    path('', views.index, name = 'index'),
    # 所有主题页
    path('topics/', views.topics, name='topics'),
    # 特定肢体详细页
    path('topics/<topic_id>/', views.topic, name = 'topic'),
    # 用于添加主题的页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry')
]