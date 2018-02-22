from django.db import models
from datetime import datetime

# Create your models here.
NEW_TYPE = (
    ('gs', '公司新闻'),
    ('hy', '行业新闻'),
    ('jt', '家庭教育'),
)


class News(models.Model):
    name = models.CharField(max_length=50, verbose_name='新闻标题')
    type = models.CharField(choices=NEW_TYPE, max_length=5, verbose_name="新闻类型")
    content = models.TextField(verbose_name="内容")
    author = models.CharField(max_length=10, verbose_name='作者')
    wahch_nums = models.IntegerField(default=0, verbose_name="浏览次数")
    add_time = models.DateField(default=datetime.now, verbose_name="发表时间")

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
