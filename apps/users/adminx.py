# coding:utf-8
__author__ = "dfk"
__date__ = "2018/2/9 17:12"
import xadmin
from xadmin import views

from .models import EmailVerifyRecord


class BaseSetting(object):
    """
    使用主题
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    修改xadmin一些配置
    """
    site_title = "dfk在线教育网"
    site_footer = '在线教育网'
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['email']
    search_fields = ['email']
    list_filter = ['email']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
