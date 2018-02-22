from django.db import models
from datetime import datetime

# Create your models here.

EDUCATION = (
    ("xx", "小学"),
    ("cz", "初中"),
    ("gz", "高中"),
    ("dx", "大学"),
)


class Education(models.Model):
    name = models.CharField(choices=EDUCATION, max_length=3)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "学历"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_grade(self):
        return self.grade_set.all()


class Grade(models.Model):
    name = models.CharField(max_length=20, verbose_name="年级")
    education = models.ForeignKey(Education, verbose_name="学历")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "年级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=10, verbose_name="科目名")
    education = models.ForeignKey(Education, null=True, blank=True, verbose_name="学历")
    grade = models.ForeignKey(Grade, null=True, blank=True, verbose_name="年级")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "科目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


TEACH_WAY = (
    ("one to one", "一对一"),
    ("one to two", "一对二"),
    ("one to three", "一对三"),
    ("small people", "小班"),
)


class CityDict(models.Model):
    name = models.CharField(max_length=10,verbose_name="城市")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Courses(models.Model):
    education = models.ForeignKey(Education, null=True, blank=True, verbose_name="学历")
    grade = models.ForeignKey(Grade, null=True, blank=True, verbose_name="年级")
    lesson = models.ForeignKey(Lesson, null=True, blank=True, verbose_name="科目")
    city = models.ForeignKey(CityDict, null=True, blank=True, verbose_name="城市")

    name = models.CharField(max_length=50, verbose_name="课程名")
    shop_price = models.IntegerField(verbose_name="市场价格")
    py_price = models.IntegerField(verbose_name="便宜价格")
    lessons = models.IntegerField(verbose_name="课次")
    people = models.IntegerField(verbose_name="开课人数")
    open_time = models.CharField(max_length=20, verbose_name="开课时间")
    desc = models.TextField(verbose_name="课程介绍")
    teach_desc = models.TextField(verbose_name="教学内容")
    teach_feature = models.TextField(verbose_name="教学特定")
    teach_target = models.TextField(verbose_name="教育目标")
    image = models.ImageField(max_length=200, upload_to="courses/%Y/%m")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    std_num = models.IntegerField(default=0, verbose_name="学习人数")
    is_fun = models.BooleanField(default=False, verbose_name="是否周末")
    teach_way = models.CharField(choices=TEACH_WAY, max_length=15, verbose_name="授课方式")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
