from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  # User facing pages
  # path('',user.login,name="login"),
  # path('userhome',user.userhome,name="userhome"),
  # path('studenthome',Fstudent.studenthome,name="studenthome"),
  # path('tutorhome',Ftutor.tutorhome,name="tutorhome"),
  # path('tutorsessions',Fstudent.showtutorSessions,name='tutorsession'),
  # path('tutorOrghome',FtutorOrg.tutorOrghome,name='tutorOrghome'),
  # path('createSession',FtutorOrg.createSession,name='createSession'),
  
  #these are for the API
  path('user/', UserList.as_view()),
  path('user/<str:pk>/', UserDetail.as_view()),
  path('student/', StudentList.as_view()),
  path('student/<str:pk>/', StudentDetail.as_view()),
  path('tutor/', TutorList.as_view()),
  path('tutor/<str:pk>/', TutorDetail.as_view()),
  path('tutororgman/', TutorOrgManList.as_view()),
  path('tutororgman/<str:pk>/', TutorOrgManDetail.as_view()),
  path('tutorsession/', TutorSessionList.as_view()),
  path('tutorsession/<str:pk>/', TutorSessionDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)