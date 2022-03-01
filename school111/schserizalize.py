from rest_framework import serializers
from .models import Student, Teacher, learn
from django import views

"""
    关联查找，是根据表本身的外键去查找，关联其他的表数据
"""


class StudentModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class LearntModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = learn
        fields = ["cname", "sno"]


class StudentLearnModelSerialize(serializers.ModelSerializer):
    learn1 = LearntModelSerialize(many=True, read_only=True)
    print(learn1)
    class Meta:
        model = Student
        fields = ["sno", "sname"]


class Student2ModelSerizalize(serializers.ModelSerializer):
    sname = serializers.StringRelatedField(many=True)
    class Meta:
        model = learn
        # fields = ["id", "sname", "cname"]
        fields = "__all__"
        depth = 1

