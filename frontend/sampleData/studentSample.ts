import Student from '../classes/Student';
const studentData = [
  {
      "studentID": "3dfabc08-935d-4d72-9129-fb7c6288e1a5",
      "yearInSchool": 2
  },
  {
      "studentID": "403d1f83-a859-490c-9670-f668637e0edc",
      "yearInSchool": 1
  },
  {
      "studentID": "0cc36d8c-7786-4fe5-9675-ebf74fe30c9a",
      "yearInSchool": 3
  },
  {
      "studentID": "0597aab6-14d3-4dbc-a0ac-f4c9658de17e",
      "yearInSchool": 2
  },
  {
      "studentID": "4ed13553-0c5a-476f-af0a-81ed3d5d60bc",
      "yearInSchool": 1
  },
  {
      "studentID": "e72bb5b7-0712-4911-b3b6-8b57da54f267",
      "yearInSchool": 4
  },
  {
      "studentID": "10fc9eee-0a17-47f7-aa5f-24b6de6fec4b",
      "yearInSchool": 1
  },
  {
      "studentID": "d872298c-7b72-490b-b8f8-f071d360da69",
      "yearInSchool": 3
  },
  {
      "studentID": "e3d48408-7de8-4234-a412-579d6af944e0",
      "yearInSchool": 4
  },
  {
      "studentID": "a6855857-567e-4862-af15-1673a1df3da7",
      "yearInSchool": 0
  },
  {
      "studentID": "f1dd50bf-06d2-4d7c-a6ac-9d8a4160ff92",
      "yearInSchool": 4
  },
  {
      "studentID": "2452bc39-dbf2-4ed1-bb9c-ea959ad7558f",
      "yearInSchool": 1
  },
  {
      "studentID": "f642c8f3-6acf-49eb-8228-4fd9689bba65",
      "yearInSchool": 5
  },
  {
      "studentID": "766229cc-5af9-4c78-a47f-4d9785fa2d5c",
      "yearInSchool": 5
  },
  {
      "studentID": "eb83af16-e404-4808-bfc1-8c00dc0520a4",
      "yearInSchool": 1
  },
  {
      "studentID": "11035083-fa99-4f9b-86de-3365d8a230de",
      "yearInSchool": 5
  },
  {
      "studentID": "2c623ac3-ad70-47cf-a358-cb1dbe3feafd",
      "yearInSchool": 1
  },
  {
      "studentID": "8d4e2753-ef26-45b7-8e49-df560b648acd",
      "yearInSchool": 0
  },
  {
      "studentID": "deffed7a-d728-4256-a0ca-35ab38553ac8",
      "yearInSchool": 2
  },
  {
      "studentID": "a2834536-95de-4d6e-9df2-e07353f04099",
      "yearInSchool": 0
  },
  {
      "studentID": "989bb030-86c4-4b06-86a8-e22fd57caf0d",
      "yearInSchool": 2
  },
  {
      "studentID": "606375b8-bb93-4826-bcee-9d29ce4f1ca0",
      "yearInSchool": 0
  },
  {
      "studentID": "afd4fc7b-ef20-4346-832f-b3088d56206d",
      "yearInSchool": 0
  },
  {
      "studentID": "c9d0a7f4-0042-4fc6-ab87-71dffccae6b8",
      "yearInSchool": 1
  },
  {
      "studentID": "8772c347-5cba-4be3-8404-64c0e65a3ae4",
      "yearInSchool": 1
  },
  {
      "studentID": "79460978-65e9-4753-8638-9bd3d26eeeba",
      "yearInSchool": 4
  },
  {
      "studentID": "c399fd7f-b75d-471e-a453-1fe9b48f653e",
      "yearInSchool": 5
  },
  {
      "studentID": "59cd012a-06b4-4b6f-9f94-e3c818a77594",
      "yearInSchool": 0
  },
  {
      "studentID": "259a2b28-b22b-4974-8c5c-192ff1c51dda",
      "yearInSchool": 1
  },
  {
      "studentID": "e0acf9ff-88d3-481a-9b4e-1428a0483bb2",
      "yearInSchool": 0
  }
];
const studentMap = new Map<string, Student>(
  studentData.map((student) => {
    return [student.studentID, new Student(student.studentID, student.yearInSchool)];
  })
);
const studentArray = Array.from(studentMap.values());

export {studentMap, studentArray};
