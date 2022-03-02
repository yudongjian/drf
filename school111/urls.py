"""drfdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import StudentView, StudentList, StudentInfo, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, StudentModelViewSet
urlpatterns = [
    path('s1/', StudentView.as_view()),
    path('s2/', StudentList.as_view()),
    path('s3/<int:index>/', StudentInfo.as_view()),
    path('s4/', StudentListCreateAPIView.as_view()),
    path('s4/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('s5/', StudentModelViewSet.as_view({"get": "list", "post": "create"})),
    path('s5/<int:pk>/', StudentModelViewSet.as_view({"get": "retrieve", "put":"update", "delete": "destroy"})),

]

# 路由集类，可配合视图集类使用，更为的方便
# DefaultRouter 开发调试使用  SimpleRouter 上线应用使用
from rest_framework.routers import DefaultRouter, SimpleRouter
router = DefaultRouter()
router.register("s6", StudentModelViewSet, "s7")
urlpatterns += router.urls
