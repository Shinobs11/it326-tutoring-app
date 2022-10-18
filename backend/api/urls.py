from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.views import UserDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
  path('user/', UserList.as_view()),
  path('user/<int:pk>/', UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)