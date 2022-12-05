import Tutor from '../classes/Tutor';
const tutorData = [
  {
      "tutorID": "e61a441c-12e0-48b2-bad6-40fb19488dec"
  },
  {
      "tutorID": "30e9c5cc-101f-4ccc-9ed7-33e8b421eaeb"
  },
  {
      "tutorID": "cc457821-98a6-416d-9775-336d71eacd05"
  },
  {
      "tutorID": "b341facd-ff0a-40f1-a425-799aa905d750"
  },
  {
      "tutorID": "d69c91c2-7860-4602-bb4a-06cbe786ab37"
  },
  {
      "tutorID": "ec3aa314-da9b-4017-b9c1-47c719a5711b"
  },
  {
      "tutorID": "756b0715-e718-4322-a4e6-95c9b65d1226"
  },
  {
      "tutorID": "bb0378eb-7a62-422e-9d69-d9fc4b1cb8bd"
  },
  {
      "tutorID": "dd138266-d26d-4396-9058-fe8c1d7173e5"
  },
  {
      "tutorID": "6c596216-ae0f-4bc8-a36b-cb0167e98363"
  },
  {
      "tutorID": "6af79ad2-993e-48c6-a6b1-06e289110af0"
  },
  {
      "tutorID": "9d44c93e-7799-48e2-b368-c5539c30ceaa"
  },
  {
      "tutorID": "eecb325b-064f-468d-b080-e0035e7f503c"
  },
  {
      "tutorID": "efe6171b-5723-4959-b415-1accf5a3e893"
  },
  {
      "tutorID": "affe2554-e5ae-4699-a5e3-a7196bf52dfd"
  },
  {
      "tutorID": "3d6e2667-b665-4d6e-9f39-ccaa580c79fc"
  },
  {
      "tutorID": "7d718591-3fee-4fc7-ae2d-ffdff57b8a92"
  },
  {
      "tutorID": "ff4533fe-bc6f-46ac-a139-d15d48d8b9ef"
  },
  {
      "tutorID": "813dd49a-8d99-443c-83f7-ba05cf4bb315"
  },
  {
      "tutorID": "9db3466d-1ba6-4c61-aaf9-4919e69b7971"
  },
  {
      "tutorID": "b9cde60c-ab1e-4794-b0f2-297adceb2013"
  },
  {
      "tutorID": "22c71d04-6c32-4aff-a9fa-4ea6f8db1a4d"
  },
  {
      "tutorID": "a9774b71-de6d-4d7e-9f31-2acb2362dbc1"
  },
  {
      "tutorID": "c74dd25c-6dbf-459c-837d-975248f3531c"
  },
  {
      "tutorID": "3a72017d-c29e-4120-8ddb-2316cc68fd3f"
  },
  {
      "tutorID": "53ff6644-4741-4e56-b5e2-834d907d8532"
  },
  {
      "tutorID": "c1b5468a-27bb-4580-a8f5-8c5dffa08419"
  },
  {
      "tutorID": "5b8c4949-1068-41d3-a33d-9c54f30459cc"
  },
  {
      "tutorID": "28280370-5672-4bc7-a06e-8502002f9cc4"
  },
  {
      "tutorID": "f6d080c4-6409-4f32-8c4e-66dade0989b9"
  }
]

const tutorMap = new Map<string, Tutor>(
  tutorData.map((tutor) => [tutor.tutorID, new Tutor(tutor.tutorID)])
);

const tutorArray = Array.from(tutorMap.values());

export {tutorMap, tutorArray};