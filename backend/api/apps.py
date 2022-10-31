from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # def ready(self):
      
      # if os.environ.get('RUN_MAIN', None) != 'true':  
        # models = AppConfig.get_models(self)
        # print([mod._meta.model_name for mod in models])


        



