# coding:utf-8
__author__ = "dfk"
__date__ = "2018/2/12 11:34"

from django.conf.urls import url
from .views import CategoryDetailView, CategoryListView, TeacherDetailView, TeacherListView

app_name = 'category'

urlpatterns = [
    # 分校 讲师
    url('^list/$', CategoryListView.as_view(), name="cat_list"),
    url('^detail/(?P<cat_id>\d+)$', CategoryDetailView.as_view(), name="cat_detail"),
    url('^tea_list/$', TeacherListView.as_view(), name="tea_list"),
    url('^tea_detail/(?P<tea_id>\d+)$', TeacherDetailView.as_view(), name="tea_detail"),
]
