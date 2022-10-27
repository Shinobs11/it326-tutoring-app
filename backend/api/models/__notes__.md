### Relationship errors
When working with the models and dealing with relationships between tables (as is the case between User and Student, Tutor and TutorOrgManager) there is a bit of a bug where for whatever reason the import of a model class is instead considered a module and doesn't play nice with Django.

Example
----
```
from api.models import User

...

user = models.OneToOneField(User, ...)
```
This will throw an error because of the way the User is imported. The workaround for this is to either 
A. Directly import User
```
from api.models.User import User

...

user = models.OneToOneField(User, ...)

```
or B. use the model name as a string as is done here https://stackoverflow.com/questions/35459326/foreignkey-to-a-model-that-is-defined-after-below-the-current-model

```
from api.models import User

...

user = models.OneToOneField('User', ...)

```