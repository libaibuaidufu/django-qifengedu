# coding:utf-8
__author__ = "dfk"
__date__ = "2018/2/9 17:12"
import xadmin
from xadmin import views

from .models import Education, Grade, Lesson, Courses, CityDict


class EducationAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class GradeAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class LessonAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CoursesAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CityDictAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(Education, EducationAdmin)
xadmin.site.register(Grade, GradeAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Courses, CoursesAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
