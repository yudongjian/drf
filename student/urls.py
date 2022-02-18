from django.urls import path
from . import views
urlpatterns = [
    path('s1/', views.BookViews.as_view())
]