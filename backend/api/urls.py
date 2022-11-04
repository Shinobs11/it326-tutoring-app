from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.views import UserDetail, UserList, StudentDetail, StudentList, TutorList, TutorDetail, TutorOrgManDetail, TutorOrgManList
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
  path('user/', UserList.as_view()),
  path('user/<str:pk>/', UserDetail.as_view()),
  path('student/', StudentList.as_view()),
  path('student/<str:pk>/', StudentDetail.as_view()),
  path('tutororgman/', TutorOrgManList.as_view()),
  path('tutororgman/<str:pk>/', TutorOrgManDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)