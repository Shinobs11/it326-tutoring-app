from django.db import models
from api.models.User import User

class Inbox:

    class Meta:
        app_label = 'api'

        #MANDATORY 1-1 with User
        user = models.OneToOneField(User, on_delete=models.CASCADE)

