from django.db import models
from datetime import datetime


# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="机构名")
    address = models.CharField(max_length=50, verbose_name="机构地址")
    tel = models.CharField(max_length=11, verbose_name="电话号码")
    opentime = models.CharField(max_length=30, verbose_name="开课时间")
    desc = models.TextField(verbose_name="机构介绍")
    click_nums = models.IntegerField(verbose_name="机构点击量")

    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "机构信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_image(self):
        return self.categoryimage_set.all()


class CategoryImage(models.Model):
    category = models.ForeignKey(Category,null=True,blank=True, verbose_name="机构")
    image = models.ImageField(max_length=200,verbose_name="校区展示", upload_to="category/%Y/%m")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "机构图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name


class Teacher(models.Model):
    name = models.CharField(max_length=10, verbose_name="教师名")
    teach_time = models.IntegerField(max_length=10, verbose_name="教学时间")
    teach_grade = models.CharField(max_length=10, verbose_name="擅长科目")

    glory = models.CharField(max_length=200, verbose_name="教师荣誉")
    desc = models.CharField(max_length=200, verbose_name="教师介绍")
    education = models.CharField(max_length=200, verbose_name="教师背景")
    motto = models.CharField(max_length=200, verbose_name="教师格言")
    click_nums = models.IntegerField(default=0, verbose_name="点击量")

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_image(self):
        return self.teacherimage_set.all()


class TeacherImage(models.Model):
    teacher = models.ForeignKey(Teacher, null=True,blank=True,verbose_name="教师")
    image = models.ImageField(max_length=200, verbose_name="校区展示", upload_to="teacher/%Y/%m")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师风采"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher.name
