from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from .schserizalize import StudentModelSerialize, LearntModelSerialize, StudentLearnModelSerialize
from rest_framework.response import Response
from django.http.response import JsonResponse
from school111.models import Student, Teacher, learn
from .schserizalize import Student2ModelSerizalize
# Create your views here.


class StudentView(APIView):
    def get(self, request):
        Student_data = Student.objects.all()
        Student_data = StudentModelSerialize(Student_data, many=True)
        print(request.user)
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
