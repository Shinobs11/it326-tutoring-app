from django.db import models

import uuid

class TutorOrgManager(models.Model):

  class Meta:
    app_label = 'api'

  # OPTIONAL 1-1 relation with User

  tutOrgManID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True, null=False, blank=False)
