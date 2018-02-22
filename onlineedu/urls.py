"""onlineedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin
from django.views.static import serve
from django.views.generic import TemplateView
from .settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ActiveView, LogoutView
from courses.views import CourseView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 首页
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^courses/$', CourseView.as_view(), name='courses'),
    # 分校和讲师相关urls
    url(r'^category/', include('category.urls', namespace="category")),

    # 登录
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 注册
    url(r'^register/$', RegisterView.as_view(), name='register'),
    # 激活
    url(r'^active/(?P<code>.*)$', ActiveView.as_view(), name='active'),
    # 退出
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # 验证码相关urls
    url(r'^captcha/', include('captcha.urls')),
    # 媒体图片相关urls
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
