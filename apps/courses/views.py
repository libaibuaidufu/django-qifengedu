from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Courses, Education, Grade, Lesson, CityDict
from category.models import Category


# Create your views here.

# class CoursesView(View):
#     def get(self, request):
#         all_education = Education.objects.all()
#
#         edu = request.GET.get('edu', "")
#         grade_id = int(request.GET.get("grade", ""))
#         lesson_id = int(request.GET.get("lesson", ""))
#
#         # 年级变化
#         all_grade = Grade.objects.filter(education="xx")
#         if edu:
#             all_grade = Grade.objects.filter(education=edu)
#
#         # 科目变化
#         all_lesson = Lesson.objects.filter(education='xx')
#         if grade_id:
#             all_lesson = Grade.objects.filter(grade_id=grade_id, education=edu)
#
#         # 课程筛选
#         all_courses = Courses.objects.all()
#         if edu:
#             all_courses = all_courses.filter(education=edu)
#         if grade_id:
#             all_courses = all_courses.filter(grade_id=grade_id)
#         if lesson_id:
#             all_courses = all_courses.filter(lesson_id=lesson_id)
#
#         return render(request, "课程列表页面.html", {
#             "all_courses": all_courses,
#             "all_education": all_education,
#             "all_grade": all_grade,
#             "all_lesson": all_lesson,
#         })


class CourseView(View):
    def get(self, request):
        all_courses = Courses.objects.all()

        # 获取参数
        edu_id = int(request.GET.get('edu', 0))
        grade_id = int(request.GET.get("grade", 0))
        lesson_id = int(request.GET.get("lesson", 0))
        city_id = int(request.GET.get("city", 0))
        teach_way = request.GET.get("teach_way", '')
        is_fun = request.GET.get("is_fun", '')

        if edu_id:
            all_courses = all_courses.filter(education_id=edu_id)
        if grade_id:
            all_courses = all_courses.filter(grade_id=grade_id)
        if lesson_id:
            all_courses = all_courses.filter(lesson_id=lesson_id)
        if city_id:
            all_courses = all_courses.filter(city_id=city_id)
        if teach_way:
            all_courses = all_courses.filter(teach_way=teach_way)
        if is_fun:
            all_courses = all_courses.filter(is_fun=is_fun)

        sort = request.GET.get('sort', '')
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by('-people')
            elif sort == 'courses':
                all_courses = all_courses.order_by('-add_time')
            elif sort == 'price':
                all_courses = all_courses.order_by('-py_price')
        # 搜索筛选
        key_word = request.GET.get('keyword', '')
        if key_word:
            all_courses = all_courses.filter(Q(name__icontains=key_word) | Q(desc__icontains=key_word))

        # 所有学历
        all_education = Education.objects.all()
        all_grade = Grade.objects.all()
        all_lesson = Lesson.objects.all()
        all_city = CityDict.objects.all()
        # 年级筛选
        if edu_id:
            all_grade = Grade.objects.filter(education_id=edu_id)
            all_lesson = Lesson.objects.filter(education_id=edu_id)
        # 科目筛选
        if grade_id:
            all_lesson = all_lesson.filter(grade_id=grade_id)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, 1, request=request)

        all_courses = p.page(page)

        return render(request, '课程列表页面.html', {
            "all_courses": all_courses,
            "all_education": all_education,
            "all_grade": all_grade,
            "all_lesson": all_lesson,
            'all_city': all_city,
            'edu_id': edu_id,
            'grade_id': grade_id,
            'lesson_id': lesson_id,
            'city_id': city_id,
            'teach_way': teach_way,
            'is_fun': is_fun,
        })
