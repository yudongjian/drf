from rest_framework import serializers
from .models import Student, Teacher, learn
from django import views


class StudentModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class LearntModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = learn
        fields = "__all__"


class StudentLearnModelSerialize(serializers.ModelSerializer):
    learn1 = LearntModelSerialize(many=True)
    class Meta:
        model = Student
        fields = ["sno", "sname", "tno"]


