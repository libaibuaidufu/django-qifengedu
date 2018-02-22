import datetime

from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.views import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from .models import UserProfile, EmailVerifyRecord
from utils.send_emal_type import send_type_email
from news.models import News
from category.models import Category, Teacher
from courses.models import Courses


# User = get_user_model()


# Create your views here.

class CustomBackend(ModelBackend):
    """
    自定义验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveView(View):
    """
    激活
    """

    def get(self, request, code):
        all_records = EmailVerifyRecord.objects.filter(code=code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class LoginView(View):
    """
    登录
    """

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get('password', "")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form.errors})


class RegisterView(View):
    """
    注册
    """

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form})
            password = request.POST.get('password', '')
            user = UserProfile()
            user.username = user_name
            user.email = user_name
            user.password = make_password(password)
            user.is_active = False
            user.save()

            send_type_email(user_name, send_type='register')
            return render(request, "login.html", {})
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LogoutView(View):
    """
    登出
    """

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class IdnexView(View):
    """
    首页
    """

    def get(self, request):
        all_news = News.objects.all()[:5]
        all_courses = Courses.objects.all()[:8]
        all_teachers = Teacher.objects.all()[:3]
        return render(request, 'index.html', {
            'all_news': all_news,
            "all_courses": all_courses,
            'all_teachers': all_teachers
        })
