from rest_framework.authentication import BaseAuthentication

"""
 自定义用户验证
"""

class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        uesr = request.request.META.get('HTTP_X_USERNAME')