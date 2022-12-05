from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from api.Fstudent import Fstudent
from api.Ftutor import Ftutor
from api.FtutorOrg import FtutorOrg
from api.FtutorOrgManager import FtutorOrgManager
from api.FtutorSess import FtutorSession
from api.Fuser import Fuser



urlpatterns = [
  # User facing pages
  path('',Fuser.login,name="login"),
  path('createprofile',Fuser.createProfile,name="createprofile"),
  path('userhome',Fuser.userhome,name="userhome"),
  path('studenthome',Fstudent.studenthome,name="studenthome"),
  path('rateSession',Fstudent.ratePage,name='ratesession'),
  path('createRating',Fstudent.rate,name='sendrating'),
  path('tutorhome',Ftutor.tutorhome,name="tutorhome"),
  path('tutorOrgMgrHome',FtutorOrgManager.tutorOrgMgrhome,name="tutorOrgMgrHome"),
  path('tutorsessions',Fstudent.showtutorSessions,name='tutorsession'),
  path('tutorOrghome',FtutorOrg.tutorOrghome,name='tutorOrghome'),
  path('createSession',FtutorOrg.createSession,name='createSession'),
  path('CreateTutorOrg',FtutorOrgManager.createTutorOrg,name='createTutorOrg'),
  path('CreateTutorOrgPath',FtutorOrgManager.tutorOrgPath,name='createTutorOrgPath'),
  path('deleteProfile', Fuser.deleteProfile,name='deleteprofile'),
  path('deleteProfilePath', Fuser.deleteProfilePath,name='deleteprofilepath'),
  path('rateSession',Fstudent.ratePage,name='ratesession'),
  path('createRating',Fstudent.rate,name='sendrating'),
  path('RegisterforSessPath',Fstudent.registerSessPage, name='registerforsesspage'),
  path('RegisterforSess',Fstudent.registerStudentSess,name='registersess'),
  path('RemoveUserPath', FtutorOrgManager.removeUserPath, name='removeuserpath'),
  path('RemoveUser',FtutorOrgManager.removeUser,name='removeuser'),
  path('TutSesInfoPg/<tutSesID>',FtutorSession.loadSesPg,name='TutSesInfoPg'),
  path('RegisterforSessTutorPath',Ftutor.registerTutorSessPage, name='registerforsesstutpage'),
  path('RegisterforSessTutor',Ftutor.registerTutorSess,name='registersesstut'),

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
  path('tutorsession/<str:pk>/', TutorSessionDetail.as_view()),
  path('tutororganization/', TutorOrganizationList.as_view()),
  path('tutororganization/<str:pk>/', TutorOrganizationDetail.as_view()),
  path('class/', ClassList.as_view()),
  path('class/<str:pk>/', ClassDetail.as_view()),
  path('review/', ReviewList.as_view()),
  path('review/<str:pk>/', ReviewDetail.as_view()),
  path('sessionresource/', SessionResourceList.as_view()),
  path('sessionresource/<str:pk>', SessionResourceDetail.as_view())
  # path('api/tutor_session', views.TutorSession),
  # path('api/tutor_session/<str:pk>', views.)
]

urlpatterns = format_suffix_patterns(urlpatterns)