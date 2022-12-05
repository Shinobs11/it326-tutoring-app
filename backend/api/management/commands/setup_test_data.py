# https://mattsegal.dev/django-factoryboy-dummy-data.html
from django.db import transaction
from django.core.management.base import BaseCommand

from api.models import *
from api.factories.UserFactory import UserFactory
from api.factories.StudentFactory import StudentFactory
from api.factories.TutorFactory import TutorFactory
from api.factories.TutorOrgManagerFactory import TutorOrgManagerFactory
from api.factories.ClassFactory import ClassFactory
import os
from random import sample, randint
from api.utils.sample_fast import iter_sample_fast
from ...factories.TutorSessionFactory import TutorSessionFactory

from ...factories.TutorOrganizationFactroy import TutorOrganizationFactory


TOGGLE =  os.environ['GENERATE_NEW_DATA']

NUM_USERS = 60
NUM_STUDENTS = 30
NUM_TUTORS = 30
NUM_MANAGERS = 30
NUM_TUTOR_ORGS = 10
NUM_SESSIONS = 20
class Command(BaseCommand):
  help = "Generates test data"

  # Using the transaction.atomic decorator makes a big difference in the runtime of this script,
  # since it bundles up 100s of queries and submits them in one go.
  @transaction.atomic
  def handle(self, *args, **kwargs):
    # self.stdout.write("Deleting old data...")
    # models = [User, Tutor, TutorOrgManager, Student]
    # for m in models:
    #   m.objects.all().delete()
    if(not TOGGLE):
      pass

    self.stdout.write("Creating new data...")
    users: list[User] = []
    students: list[Student] = []
    tutors: list[Tutor] = []
    tutorOrgManagers: list[TutorOrgManager] = []
    student_sample = sample(range(NUM_USERS), k=NUM_STUDENTS)
    tutor_sample = sample(range(NUM_USERS), k=NUM_TUTORS)
    manager_sample = sample(range(NUM_USERS), k=NUM_MANAGERS)

    student_range = [False]*NUM_USERS
    tutor_range = [False]*NUM_USERS
    manager_range = [False]*NUM_USERS

    for i in student_sample:
      student_range[i] = True
    for i in tutor_sample:
      tutor_range[i] = True
    for i in manager_sample:
      manager_range[i] = True

    for i in range(NUM_USERS):
      users.append(UserFactory.create())
    for i in student_sample:
      students.append(StudentFactory.create(user=users[i]))
    for i in tutor_sample:
      tutors.append(TutorFactory.create(user=users[i]))
    for i in manager_sample:
      tutorOrgManagers.append(TutorOrgManagerFactory.create(user=users[i]))
    

    tutorOrgs: list[TutorOrganization] = []
    orgTutorSample:list[list[Tutor]] = [sample(tutors, k=randint(0, 9)) for _ in range(NUM_TUTOR_ORGS)]
    orgManagerSample:list[list[TutorOrgManager]] = [sample(tutorOrgManagers, k=randint(1,3)) for _ in range(NUM_TUTOR_ORGS)]
    for i in range(NUM_TUTOR_ORGS):
      tutorOrgs.append(TutorOrganizationFactory.create())
      tutorOrgs[i].tutor.set(orgTutorSample[i])
      tutorOrgs[i].tutOrgMan.set(orgManagerSample[i])




    wordlist = ['IT', 'MAT', 'PHYS', 'ENGR', 'GEO', 'SOC'];
    
    def generateClassNameSet(word:str):
      multiplier = randint(0, 4)
      count = randint(4, 20)
      postfix_sample = [str(100*multiplier + randint(0, 99) + i) for i in range(count)]
      return [f"{word} {postfix}" for postfix in postfix_sample]
    class_name_sets = [generateClassNameSet(word) for word in wordlist];

    class_sets: list[list[Class]] = []
    for set in class_name_sets:
      class_instance_set = []
      for name in set:
        class_instance_set.append(ClassFactory.create(className=name))
      class_sets.append(class_instance_set)

    

    sessions: list[TutorSession] = []
    
    for i in range(NUM_SESSIONS):
      tutorOrg = sample(tutorOrgs, k=1)[0]
      sessions.append(TutorSessionFactory.create(tutorOrgID=tutorOrg))
      session_tutors = iter_sample_fast(tutorOrg.tutor.get_queryset(), randint(0, tutorOrg.tutor.count()))
      session_students = sample(students, k=randint(1, 20))
      set = sample(class_sets, k=1)[0]
      class_sample = sample(set, k=randint(1, len(set)))
      sessions[i].tutor.set(session_tutors)
      sessions[i].student.set(session_students)
      sessions[i].classID.set(class_sample)




# https://stackoverflow.com/questions/66381042/how-to-assign-the-attribute-of-subfactory-instead-of-the-subfactory-itself
# https://factoryboy.readthedocs.io/en/latest/reference.html#maybe


    

