from django.contrib import admin
from django.urls import path
from app1.views import index, task1, task2, task3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('task1/', task1),
    path('task2/', task2),
    path('task3/', task3)
]
