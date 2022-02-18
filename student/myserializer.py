from rest_framework import serializers
# Create your views here.
from .models import Book

class BookSerializer(serializers.Serializer):
    def check_fun1(self, data):
        return data

    # read_only 设置只在序列化时使用，反序列化不需要使用
    # max_value, max_length
    # required 是否是必须字段
    # default 默认字段
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    price = serializers.IntegerField(max_value=99)
    # 这是另一种数据验证方法， validators 可以传递一个函数列表,即可以传递多个函数进行验证
    # 一般有通用的验证方法时，用这个验证方法，实际很少使用到。
    # price = serializers.IntegerField(validators=[check_fun1])
    category = serializers.CharField(max_length=20)
    author = serializers.CharField()

    # 以下进行数据验证

    # 验证方法一: 单个字段进行验证
    def validate_price(self, data):
        if data > 99:
            raise serializers.ValidationError('对不起,该书籍太贵，不宜上架！！！')
        return data

    # 验证方法二： 多个字段进行验证
    # def validate(self, attrs):
    #     if "黄" in str(attrs.get('title')):
    #         raise serializers.ValidationError('对不起，该书包含敏感词汇...')
    #     return attrs

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        instance.category = validated_data.get('category')
        instance.save()
        return instance