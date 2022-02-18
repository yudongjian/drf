from django.shortcuts import render
from .myserializer import BookSerializer
from django.views import View
from student.models import Book
from django.http.response import JsonResponse


class BookViews(View):

    # 1、查询数据
    # 2、实例化化序列化器，并传入待序列化的数据
    # 3、返回json数据

    """
    BookSerializer 包含四个参数

        instance: 第一个参数 可以不填写
        data: 可以是接收到网页的数据，用于更新
        many: True False 是否多条数据
    """

    # 查询单条数据
    def get1(self, request):
        book = Book.objects.first()
        book = BookSerializer(book)
        print(book)
        print(book.data)
        # book.data 是一个OrderedDict对象，有序字典，是python的高级数据类型，
        # 主要是解决dict在存储数据时的随机性问题，用法和dict一致
        return JsonResponse(book.data)

    # 查询多条数据
    def get2(self, request):
        book_datas = Book.objects.all()
        book_datas = BookSerializer(instance=book_datas, many=True)
        print(book_datas.data)

        return JsonResponse(book_datas.data, safe=False)

    # 插入数据
    def get3(self, request):
        mydict={
            "title": "红楼梦",
            "category": "古典文学",
            "price": 59,
            "author": "曹雪芹"
        }
        book = BookSerializer(data=mydict)
        book.is_valid(raise_exception=True)
        book.save()
        print(book.data)
        return JsonResponse(book.data, safe=False)

    # 更新数据
    def get(self, request):
        now_id = 10
        mydict = {
            "title": "石头记",
            "category": "小说",
            "price": 29,
            "author": "小小芹"
        }
        old_book = Book.objects.get(id=now_id) # git得到的是一个模型，而filter得到的是QuerySet

        serializer = BookSerializer(instance=old_book, data=mydict)
        # 可以只更新局部数据，只在更新时有效，绕过required字段, 只在特殊场景下使用！！！
        # serializer = BookSerializer(instance=old_book, data=mydict, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data)