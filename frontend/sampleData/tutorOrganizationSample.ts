import getSample from "../utils/getSample"
import { userArrayByTutor, userArrayByTutorOrgManager } from "./userSample"
import { TutorOrganization } from "../classes"

const tutorOrganizationData = [
  {
    "orgID": 1,
    "name": "Tutoring Organization 1",
    "description": "This is a description of Tutoring Organization 1",
    "tutors": getSample(userArrayByTutor, 10),
    "managers": getSample(userArrayByTutorOrgManager, 3)
  },
  {
    "orgID": 2,
    "name": "Tutoring Organization 2",
    "description": "This is a description of Tutoring Organization 2",
    "tutors": getSample(userArrayByTutor, 8),
    "managers": getSample(userArrayByTutorOrgManager, 2)
  },
  {
    "orgID": 3,
    "name": "Tutoring Organization 3",
    "description": "This is a description of Tutoring Organization 3",
    "tutors": getSample(userArrayByTutor, 5),
    "managers": getSample(userArrayByTutorOrgManager, 1)
  },
  {
    "orgID": 4,
    "name": "Tutoring Organization 4",
    "description": "This is a description of Tutoring Organization 4",
    "tutors": getSample(userArrayByTutor, 10),
    "managers": getSample(userArrayByTutorOrgManager, 1)
  },
  {
    "orgID": 5,
    "name": "Tutoring Organization 5",
    "description": "This is a description of Tutoring Organization 5",
    "tutors": getSample(userArrayByTutor, 10),
    "managers": getSample(userArrayByTutorOrgManager, 4)
  },
  {
    "orgID": 6,
    "name": "Tutoring Organization 6",
    "description": "This is a description of Tutoring Organization 6",
    "tutors": getSample(userArrayByTutor, 10),
    "managers": getSample(userArrayByTutorOrgManager, 1)
  },
  {
    "orgID": 7,
    "name": "Tutoring Organization 7",
    "description": "This is a description of Tutoring Organization 7",
    "tutors": getSample(userArrayByTutor, 10),
    "managers": getSample(userArrayByTutorOrgManager, 3)
  },
  {
    "orgID": 8,
    "name": "Tutoring Organization 8",
    "description": "This is a description of Tutoring Organization 8",
    "tutors": getSample(userArrayByTutor, 10),
    "managers": getSample(userArrayByTutorOrgManager, 3)
  }
];



const tutorOrganizationSample = tutorOrganizationData.map((tutorOrg) => {
  return new TutorOrganization(tutorOrg.orgID, tutorOrg.name, tutorOrg.description, tutorOrg.tutors, tutorOrg.managers)
});

export {tutorOrganizationSample}