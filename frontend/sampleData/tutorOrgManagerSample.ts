import { TutorOrgManager } from "../classes"
const tutorOrgManagerData = [
  {
      "tutOrgManID": "5e82501f-935b-4d11-99d1-b420a8344020"
  },
  {
      "tutOrgManID": "6cdb3b93-1370-4e9d-9282-c38728df5dc2"
  },
  {
      "tutOrgManID": "e70f10fd-8399-4bfb-b996-84d73c137826"
  },
  {
      "tutOrgManID": "52c41b06-0f38-42b2-95d6-158e5c128440"
  },
  {
      "tutOrgManID": "15d05543-af83-48f3-bb33-b0aaedc5b473"
  },
  {
      "tutOrgManID": "c8482411-bda3-4da6-ab88-88beec46c06f"
  },
  {
      "tutOrgManID": "ba91beeb-567a-46bb-853c-fdde26c63718"
  },
  {
      "tutOrgManID": "c4d3bf6e-7ca3-44d1-b24e-438082c2cd8b"
  },
  {
      "tutOrgManID": "9645a6fb-3265-4ac2-a570-7e038b42435a"
  },
  {
      "tutOrgManID": "9260c46c-2ffd-4a42-a7a7-a4067f537f94"
  },
  {
      "tutOrgManID": "269d2c4f-00d3-437d-a2d8-1c2321a558d6"
  },
  {
      "tutOrgManID": "197c8bd0-1cf5-4333-957b-08ad9cf77b38"
  },
  {
      "tutOrgManID": "3059a91b-924d-4dae-aa09-45663863aa11"
  },
  {
      "tutOrgManID": "9f591444-c27e-455c-a42f-585b780b1830"
  },
  {
      "tutOrgManID": "13f5ce6f-b053-405e-bad7-f7fd57afcb8c"
  }
]

const tutorOrgManagerMap = new Map<string, TutorOrgManager>(
  tutorOrgManagerData.map((tutorOrgManager) => {
    return [tutorOrgManager.tutOrgManID, new TutorOrgManager(tutorOrgManager.tutOrgManID)]
  })
);

const tutorOrgManagerArray = Array.from(tutorOrgManagerMap.values());

export { tutorOrgManagerMap, tutorOrgManagerArray };