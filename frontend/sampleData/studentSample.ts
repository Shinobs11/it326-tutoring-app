import Student from '../classes/Student';
const studentData = [
  {
      "studentID": "95116ed7-7e3d-497d-9229-15156807715d",
      "yearInSchool": 1
  },
  {
      "studentID": "c1ecc1b6-7bfd-4d72-bb35-d4462a39eddf",
      "yearInSchool": 2
  },
  {
      "studentID": "77994567-6e5e-474b-8a4e-8479bb8efd87",
      "yearInSchool": 1
  },
  {
      "studentID": "df673db1-c991-4c1c-a960-77c2f1a3cc45",
      "yearInSchool": 5
  },
  {
      "studentID": "485c45ee-6919-472e-92e9-264264f4e49f",
      "yearInSchool": 2
  },
  {
      "studentID": "71f364ba-4846-42f4-ab8e-5cd92d867492",
      "yearInSchool": 5
  },
  {
      "studentID": "790b9862-4891-4038-ae5d-80d5a8baf1b0",
      "yearInSchool": 2
  },
  {
      "studentID": "875f0b6a-daac-4ca7-9878-7d26b788c3b5",
      "yearInSchool": 0
  },
  {
      "studentID": "a58feb0c-66fd-4494-8c01-60e459c50268",
      "yearInSchool": 1
  },
  {
      "studentID": "8dbb491c-7e1c-4396-bd12-2d7c90a0a2d7",
      "yearInSchool": 0
  },
  {
      "studentID": "ff5f3154-d485-4357-ba66-72cccf339465",
      "yearInSchool": 5
  },
  {
      "studentID": "2717b29e-e915-420c-bf9f-fda2a17c01fd",
      "yearInSchool": 4
  },
  {
      "studentID": "2fa3e084-276d-4d01-b80d-6c780b7e6250",
      "yearInSchool": 2
  },
  {
      "studentID": "3caff8eb-2f47-4537-af85-62e2bf47caf7",
      "yearInSchool": 2
  },
  {
      "studentID": "8639bc11-4672-4227-b8d1-18056433f2f2",
      "yearInSchool": 2
  }
];
const studentMap = new Map<string, Student>(
  studentData.map((student) => {
    return [student.studentID, new Student(student.studentID, student.yearInSchool)];
  })
);
const studentArray = Array.from(studentMap.values());

export {studentMap, studentArray};
