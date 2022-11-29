import Tutor from '../classes/Tutor';
const tutorData = [
  {
      "tutorID": "fa7b12ae-092e-4db4-9945-9607b0ee9b28"
  },
  {
      "tutorID": "b9a5fbac-0893-48d5-80b7-0c520db3ad75"
  },
  {
      "tutorID": "06edfa00-6832-4a80-9860-d3e304bac8a2"
  },
  {
      "tutorID": "91dcef25-893e-4346-b5a3-5407df91c1fb"
  },
  {
      "tutorID": "1f3699b4-18d2-4bad-beaf-c047a1aac07b"
  },
  {
      "tutorID": "427609c4-7690-46fc-b378-71306d9e6a69"
  },
  {
      "tutorID": "d0a30558-78a6-4050-aa2c-d349de9021ca"
  },
  {
      "tutorID": "029977b9-4aac-446d-ad05-5530b837396b"
  },
  {
      "tutorID": "7235051b-5860-47a9-92ff-414ad197070e"
  },
  {
      "tutorID": "a0747f33-871f-4d31-bf03-718d8fb262c2"
  },
  {
      "tutorID": "46dfe3ef-e568-4916-a2e6-a4c9fb24a0df"
  },
  {
      "tutorID": "bcbacec8-4e19-4f1b-993f-7abeb106147b"
  },
  {
      "tutorID": "05288a80-b8d2-480b-a6b3-fa93a73a1a40"
  },
  {
      "tutorID": "e6dae9eb-d13e-4c73-ab03-192189eb5a15"
  },
  {
      "tutorID": "1385cc5c-ea03-4d23-9b08-671c2febce90"
  }
]

const tutorMap = new Map<string, Tutor>(
  tutorData.map((tutor) => [tutor.tutorID, new Tutor(tutor.tutorID)])
);

const tutorArray = Array.from(tutorMap.values());

export {tutorMap, tutorArray};