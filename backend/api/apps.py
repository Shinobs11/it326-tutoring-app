from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
      if os.environ.get('RUN_MAIN', None) != 'true':  
        from api.models import User
        for x in range(0, 10):
          user = User(
            first_name=f"First {x}",
            last_name=f"Last {x}",
            email_address=f"Email{x}@{x}.com",
            phone_number=f"123456789"
          )

        



