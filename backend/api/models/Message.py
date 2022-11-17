from django.db import models
from api.models.Inbox import Inbox

class Message:

    class Meta:
        app_label = 'api'

    #PK
    messageID = models.PositiveSmallIntegerField(primary_key=True)
    text = models.CharField()
    # OPTIONAL 1-M with Inbox
    message = models.ForeignKey(Inbox, on_delete=models.CASCADE, blank=True, null=True)