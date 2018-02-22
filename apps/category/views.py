from django.shortcuts import render
from django.views import View

from .models import Category, CategoryImage, TeacherImage, Teacher


# Create your views here.

class CategoryListView(View):
    def get(self, request):
        all_category = Category.objects.all()
        sort = request.GET.get("sort", "")
        if sort == 'time':
            all_category = all_category.order_by('-add_time')
        elif sort == 'click_nums':
            all_category = all_category.order_by('-click_nums')

        return render(request, "分校列表.html", {
            "all_category": all_category,
        })


class CategoryDetailView(View):
    def get(self, request, cat_id):
        category = Category.objects.get(id=int(cat_id))

        hot_categorys = Category.objects.order_by('-click_nums')[:5]

        return render(request, '分校详情.html', {
            "category": category,
            'hot_categorys': hot_categorys,

        })


class TeacherListView(View):
    def get(self, request):
        all_teacher = Teacher.objects.all()
        sort = request.GET.get("sort", '')
        if sort == 'click_nums':
            all_teacher = all_teacher.order_by('-click_nums')
        elif sort == 'time':
            all_teacher = all_teacher.order_by('-add_time')

        return render(request, '讲师.html', {
            "all_teacher": all_teacher
        })


class TeacherDetailView(View):
    def get(self, request, tea_id):
        teacher = Teacher.objects.get(id=int(tea_id))

        hot_teachers = Teacher.objects.order_by('-click_nums')[:5]

        return render(request, '讲师详情.html', {
            "teacher": teacher,
            'hot_teachers': hot_teachers,
        })
