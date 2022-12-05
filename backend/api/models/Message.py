from django.db import models
from api.models.Inbox import Inbox

class Message(models.Model):

    class Meta:
        app_label = 'api'

    #PK
    messageID = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000)
    # OPTIONAL 1-M with Inbox
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField()