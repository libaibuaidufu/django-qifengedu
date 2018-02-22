# coding:utf-8
__author__ = "dfk"
__date__ = "2018/2/9 17:12"

import xadmin
from xadmin import views

from .models import TeacherImage, CategoryImage, Category, Teacher


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CategoryImageAdmin(object):
    list_display = ['image']
    search_fields = ['image']
    list_filter = ['image']


class TeacherAmdin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class TeacherImageAdmin(object):
    list_display = ['image']
    search_fields = ['image']
    list_filter = ['image']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(CategoryImage, CategoryImageAdmin)
xadmin.site.register(Teacher, TeacherAmdin)
xadmin.site.register(TeacherImage, TeacherImageAdmin)
