# 定义learning_logs的URL模式

# from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    #主页
    # url('^$', views.index, name = 'index' ),
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name = 'topic'),
]