from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from api.Fuser import *
from api.Fstudent import *
from api.Ftutor import *
from api.FtutorOrg import *
from api.FtutorOrgManager import *


urlpatterns = [
  # User facing pages
  path('',Fuser.login,name="login"),
  path('userhome',Fuser.userhome,name="userhome"),
  path('studenthome',Fstudent.studenthome,name="studenthome"),
  path('tutorhome',Ftutor.tutorhome,name="tutorhome"),
  path('tutorOrgMgrHome',FtutorOrgManager.tutorOrgMgrhome,name="tutorOrgMgrHome"),
  path('tutorsessions',Fstudent.showtutorSessions,name='tutorsession'),
  path('tutorOrghome',FtutorOrg.tutorOrghome,name='tutorOrghome'),
  path('createSession',FtutorOrg.createSession,name='createSession'),
  path('CreateTutorOrg',FtutorOrgManager.createTutorOrg,name='createTutorOrg'),
  
  
  #these are for the API
  path('user/', UserList.as_view()),
  path('user/<str:pk>/', UserDetail.as_view()),
  path('student/', StudentList.as_view()),
  path('student/<str:pk>/', StudentDetail.as_view()),
  path('tutor/', TutorList.as_view()),
  path('tutor/<str:pk>/', TutorDetail.as_view()),
  path('tutororgman/', TutorOrgManList.as_view()),
  path('tutororgman/<str:pk>/', TutorOrgManDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)