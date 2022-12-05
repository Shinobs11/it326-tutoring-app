import { TutorOrgManager } from "../classes"
const tutorOrgManagerData =[
  {
      "tutOrgManID": "3d15eef7-38c1-462e-9148-624feac1c14f"
  },
  {
      "tutOrgManID": "2fcd81b5-d24b-4ce4-b07b-f3262f120554"
  },
  {
      "tutOrgManID": "b29a8b06-daf6-4c5f-a577-bffac87a7463"
  },
  {
      "tutOrgManID": "35e8579a-7aaf-4e89-9fb7-97fab7d6467b"
  },
  {
      "tutOrgManID": "2b5f6932-91dc-49ef-ab21-a3f6e6fd68e8"
  },
  {
      "tutOrgManID": "753c7c99-032f-46ca-b0d9-c2aa8f837ef7"
  },
  {
      "tutOrgManID": "cad6e514-ccc1-4d51-b3f6-60d8e9f41cc0"
  },
  {
      "tutOrgManID": "a38d8afc-fdd2-4d7a-b97c-cc57ce5dc807"
  },
  {
      "tutOrgManID": "ade7cef3-7ed2-4c2f-856f-3d95e0ae1a1b"
  },
  {
      "tutOrgManID": "d9efe28b-3bcb-40b3-961d-8dcf9b8086da"
  },
  {
      "tutOrgManID": "b2ddc481-ac6d-4df8-94e5-064cb799ae8e"
  },
  {
      "tutOrgManID": "9f3dd894-b6af-48b2-aeba-42d0f8303249"
  },
  {
      "tutOrgManID": "582dd972-7a08-4ca8-9cc5-a8a0743c7e9d"
  },
  {
      "tutOrgManID": "c13e66af-3c95-40d3-be2a-ad3e82221345"
  },
  {
      "tutOrgManID": "c149fa8e-7bb8-42f1-9624-d318a32652e8"
  },
  {
      "tutOrgManID": "00109824-0a61-4be3-ab22-12c9e23b580e"
  },
  {
      "tutOrgManID": "77cb1a27-974f-4edc-a6b6-208761a53fdd"
  },
  {
      "tutOrgManID": "eee84bcb-7281-48a9-a5e4-979d6f6ddf79"
  },
  {
      "tutOrgManID": "b97fb3bb-7ecc-440c-b5ff-93f0025b7c5f"
  },
  {
      "tutOrgManID": "fea2a33a-51d1-4bcd-9a23-754bef38d426"
  },
  {
      "tutOrgManID": "89181ba3-bdee-4231-81a6-009ea8dce886"
  },
  {
      "tutOrgManID": "033c1469-4f06-4a18-b4a2-64447d3c279b"
  },
  {
      "tutOrgManID": "72ef7dce-376e-42a6-ac07-1cf1e47638ec"
  },
  {
      "tutOrgManID": "20379089-711f-410a-8b29-75c6918ff358"
  },
  {
      "tutOrgManID": "90e0172f-14dc-41bc-8aa5-658322a5a421"
  },
  {
      "tutOrgManID": "85050a17-d2e1-4d4d-bad4-c2880bf56ed8"
  },
  {
      "tutOrgManID": "a5387901-69f1-4ccd-8b4c-ba0a317eeb1d"
  },
  {
      "tutOrgManID": "b0c952af-9db3-4510-a75d-08552d5590c9"
  },
  {
      "tutOrgManID": "2353d455-90bc-4b66-a063-14505d005716"
  },
  {
      "tutOrgManID": "c96ef1a5-ac70-4464-a734-f9bbc7405255"
  }
]

const tutorOrgManagerMap = new Map<string, TutorOrgManager>(
  tutorOrgManagerData.map((tutorOrgManager) => {
    return [tutorOrgManager.tutOrgManID, new TutorOrgManager(tutorOrgManager.tutOrgManID)]
  })
);

const tutorOrgManagerArray = Array.from(tutorOrgManagerMap.values());

export { tutorOrgManagerMap, tutorOrgManagerArray };