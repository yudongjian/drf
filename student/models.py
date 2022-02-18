from django.db import models
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="图书名称")
    category = models.CharField(max_length=32, verbose_name="图书的类别")
    price = models.IntegerField(default=0, verbose_name='图书价格')
    author = models.CharField(default='', max_length=20, verbose_name='作者名称')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "01-图书表"
        db_table = verbose_name_plural


