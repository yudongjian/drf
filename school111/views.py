from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from .schserizalize import StudentModelSerialize, LearntModelSerialize
from rest_framework.response import Response
from django.http.response import JsonResponse
from school111.models import Student, Teacher, learn
from .schserizalize import Student2ModelSerizalize
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class StudentView(APIView):
    def get(self, request):
        Student_data = Student.objects.all()
        Student_data = StudentModelSerialize(Student_data, many=True)
        print(request.user)
        print(request.query_params)
        # 返回的参数
        # from rest_framework import status
        # return Response(data=, status=status.***, headers=, content_type)
        return Response(Student_data.data)

    def get2(self, request):
        Student_data = Student.objects.all()
        Student_data = StudentLearnModelSerialize(Student_data, many=True)
        print(Student_data.data)
        return JsonResponse(Student_data.data, safe=False)

    def get1(self, request):
        learn_info = learn.objects.all()
        learn_info = Student2ModelSerizalize(learn_info, many=True)
        print(learn_info.data)
        return JsonResponse(learn_info.data, safe=False)

    def post(self, request):
        print(request.data)  # 获取数据
        print(request.query_params)  # 得到查询头信息
        print(request.FILES)  # 获取上传文件
        print(request._request.META)  # 获取请求头数据
        print(request._request.META.get("HTTP_USER_AGENT"))  # 获取指定key的请求头数据
        return JsonResponse({"message": "ok"})


class StudentList(APIView):
    # 查询所有数据
    def get(self, request):
        students_info = Student.objects.all()
        students_info = StudentModelSerialize(students_info, many=True)
        return Response(students_info.data, status=status.HTTP_200_OK)

    # 新增一条数据
    def post(self, request):
        student_info = StudentModelSerialize(data=request.data)
        student_info.is_valid(raise_exception=True)
        student_info.save()
        return Response(student_info.data, status=status.HTTP_201_CREATED)


class StudentInfo(APIView):
    # 获取一个数据
    def get(self, request, index):
        try:
            single_student = Student.objects.get(sno=index)
            student_info = StudentModelSerialize(single_student)
            return Response(student_info.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"message": "该学生不存在！！！"})

    # 修改一条数据
    def put(self, request, index):
        try:
            single_student = Student.objects.get(sno=index)
            print(single_student)
            student_info = StudentModelSerialize(single_student, data=request.data)
            student_info.is_valid(raise_exception=True)
            student_info.save()
            return Response(student_info.data)
        except Student.DoesNotExist:
            return Response({"message": "该学生不存在！！！"})

    # 删除一条数据
    def delete(self, request, index):
        try:
            singe_student = Student.objects.get(sno=index)
            singe_student.delete()
            return Response({"message": "已删除！！！"})
        except Student.DoesNotExist:
            return Response({"message": "该学生不存在！！！"})


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialize


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialize

    """
        这是drf提供的视图集
        若配合drf提供的路由集使用，可使代码更加简介
    """

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialize
    # authentication_classes 是一个列表，默认是SessionAuthentication
    authentication_classes = [SessionAuthentication, ]