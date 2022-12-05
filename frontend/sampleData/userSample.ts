import { tutorMap } from "./tutorSample"
import { studentMap } from "./studentSample"
import { tutorOrgManagerMap } from "./tutorOrgManagerSample"
import {User, Student, Tutor, TutorOrgManager} from "../classes"
const userData = [
  {
      "uid": "28259b01-306c-47e6-a164-86ba9cc76843",
      "first_name": "Megan",
      "last_name": "Chang",
      "email_address": "gwilliams@example.com",
      "phone_number": "(475)938-2421x9489",
      "student": "95116ed7-7e3d-497d-9229-15156807715d",
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "45b8d2f3-2424-47f6-8467-1b572f2b376f",
      "first_name": "Kyle",
      "last_name": "Blair",
      "email_address": "thomas15@example.com",
      "phone_number": "938-778-4080x16097",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "5e82501f-935b-4d11-99d1-b420a8344020"
  },
  {
      "uid": "1d822224-290f-4368-a730-d55b8b9aa8bb",
      "first_name": "Maria",
      "last_name": "Cook",
      "email_address": "jane13@example.net",
      "phone_number": "328.711.5871",
      "student": "c1ecc1b6-7bfd-4d72-bb35-d4462a39eddf",
      "tutor": "fa7b12ae-092e-4db4-9945-9607b0ee9b28",
      "tutorOrgManager": "6cdb3b93-1370-4e9d-9282-c38728df5dc2"
  },
  {
      "uid": "819cbf75-834e-489c-a8b7-e3ef9bcbd112",
      "first_name": "Andrea",
      "last_name": "Mann",
      "email_address": "lisa83@example.net",
      "phone_number": "+1-947-196-5934",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "e70f10fd-8399-4bfb-b996-84d73c137826"
  },
  {
      "uid": "6dd4085e-7bb7-4785-a39d-d5bcd3788551",
      "first_name": "Ivan",
      "last_name": "Underwood",
      "email_address": "salazardiane@example.com",
      "phone_number": "122-018-6848",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "fa165aba-0ea4-4529-bcfa-19ae75d1f60f",
      "first_name": "Lisa",
      "last_name": "Atkinson",
      "email_address": "criley@example.com",
      "phone_number": "+1-515-917-9533x04135",
      "student": "77994567-6e5e-474b-8a4e-8479bb8efd87",
      "tutor": "b9a5fbac-0893-48d5-80b7-0c520db3ad75",
      "tutorOrgManager": "52c41b06-0f38-42b2-95d6-158e5c128440"
  },
  {
      "uid": "593bebb3-9db4-44b3-91b8-26822f582457",
      "first_name": "Marvin",
      "last_name": "Cabrera",
      "email_address": "loganmelissa@example.org",
      "phone_number": "9891013991",
      "student": null,
      "tutor": "06edfa00-6832-4a80-9860-d3e304bac8a2",
      "tutorOrgManager": "15d05543-af83-48f3-bb33-b0aaedc5b473"
  },
  {
      "uid": "a3a0c45b-fbb7-49b6-b928-6ff602734fb6",
      "first_name": "Peter",
      "last_name": "Wood",
      "email_address": "johnsonandrew@example.org",
      "phone_number": "001-173-008-6914x131",
      "student": "df673db1-c991-4c1c-a960-77c2f1a3cc45",
      "tutor": "91dcef25-893e-4346-b5a3-5407df91c1fb",
      "tutorOrgManager": null
  },
  {
      "uid": "8175b1cb-7f76-42e1-995c-bcbc32a70bd0",
      "first_name": "Kevin",
      "last_name": "Graham",
      "email_address": "gordonbenjamin@example.org",
      "phone_number": "001-634-579-2302x258",
      "student": "485c45ee-6919-472e-92e9-264264f4e49f",
      "tutor": "1f3699b4-18d2-4bad-beaf-c047a1aac07b",
      "tutorOrgManager": null
  },
  {
      "uid": "7e648ac7-b988-49dd-bb43-c8ca164e8fbc",
      "first_name": "David",
      "last_name": "Morse",
      "email_address": "alexandermaldonado@example.net",
      "phone_number": "456.428.0715x08423",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "5c641b34-2ac1-4e9a-969f-25cb08d7f7a5",
      "first_name": "Kathleen",
      "last_name": "Olson",
      "email_address": "emily99@example.org",
      "phone_number": "001-466-109-3523x376",
      "student": "71f364ba-4846-42f4-ab8e-5cd92d867492",
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "e3972195-94cd-46fa-a83b-f2c3a8112573",
      "first_name": "Nancy",
      "last_name": "Carroll",
      "email_address": "sjohnson@example.net",
      "phone_number": "(027)142-7878x90075",
      "student": "790b9862-4891-4038-ae5d-80d5a8baf1b0",
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "1f3c3c3e-130a-4155-b765-92252cccc7fe",
      "first_name": "Mary",
      "last_name": "Williams",
      "email_address": "olopez@example.org",
      "phone_number": "001-206-650-3008x9131",
      "student": null,
      "tutor": "427609c4-7690-46fc-b378-71306d9e6a69",
      "tutorOrgManager": "c8482411-bda3-4da6-ab88-88beec46c06f"
  },
  {
      "uid": "ffb573c8-fe83-41ea-bd68-2b2d207bd63b",
      "first_name": "Charlene",
      "last_name": "Gonzalez",
      "email_address": "joshua21@example.com",
      "phone_number": "(104)714-2851x2400",
      "student": "875f0b6a-daac-4ca7-9878-7d26b788c3b5",
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "1fef0ad6-f943-47fb-b3e3-ca1a6544229d",
      "first_name": "Jamie",
      "last_name": "Green",
      "email_address": "stacey90@example.net",
      "phone_number": "001-977-658-2369x402",
      "student": "a58feb0c-66fd-4494-8c01-60e459c50268",
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "70e69f3d-0549-4f60-a40f-f6b14fb70757",
      "first_name": "Joseph",
      "last_name": "Morgan",
      "email_address": "jennifer59@example.org",
      "phone_number": "4229456824",
      "student": "8dbb491c-7e1c-4396-bd12-2d7c90a0a2d7",
      "tutor": "d0a30558-78a6-4050-aa2c-d349de9021ca",
      "tutorOrgManager": "ba91beeb-567a-46bb-853c-fdde26c63718"
  },
  {
      "uid": "5cf73fb6-d816-4435-a745-31083e6c0a50",
      "first_name": "Timothy",
      "last_name": "Allen",
      "email_address": "parkermelody@example.net",
      "phone_number": "465-461-1877",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "c4d3bf6e-7ca3-44d1-b24e-438082c2cd8b"
  },
  {
      "uid": "6eff27f2-2dbc-4eb9-a372-0341077ab0dd",
      "first_name": "Matthew",
      "last_name": "Yates",
      "email_address": "david17@example.com",
      "phone_number": "4522961113",
      "student": "ff5f3154-d485-4357-ba66-72cccf339465",
      "tutor": null,
      "tutorOrgManager": "9645a6fb-3265-4ac2-a570-7e038b42435a"
  },
  {
      "uid": "9e929e4b-37e0-4d51-a96b-22a2da7723d2",
      "first_name": "Jeffrey",
      "last_name": "Cruz",
      "email_address": "longapril@example.com",
      "phone_number": "936.153.4926x3511",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "9cdd49cc-35d7-435a-af78-db2975da549b",
      "first_name": "Lynn",
      "last_name": "Farrell",
      "email_address": "leachshannon@example.net",
      "phone_number": "176.430.3921",
      "student": null,
      "tutor": "029977b9-4aac-446d-ad05-5530b837396b",
      "tutorOrgManager": null
  },
  {
      "uid": "581a3d35-cc30-4682-8ee6-570250975869",
      "first_name": "James",
      "last_name": "Gray",
      "email_address": "danielcarlson@example.com",
      "phone_number": "(966)875-7738",
      "student": "2717b29e-e915-420c-bf9f-fda2a17c01fd",
      "tutor": "7235051b-5860-47a9-92ff-414ad197070e",
      "tutorOrgManager": null
  },
  {
      "uid": "99a23e65-cbfa-42ad-bebb-aeb66d5b3270",
      "first_name": "Sarah",
      "last_name": "Smith",
      "email_address": "lisa08@example.org",
      "phone_number": "926-947-1180x132",
      "student": null,
      "tutor": "a0747f33-871f-4d31-bf03-718d8fb262c2",
      "tutorOrgManager": null
  },
  {
      "uid": "58bc22e6-585c-4bf5-b94d-59580cae32b4",
      "first_name": "Billy",
      "last_name": "Smith",
      "email_address": "krivera@example.org",
      "phone_number": "+1-758-688-0918x9163",
      "student": "2fa3e084-276d-4d01-b80d-6c780b7e6250",
      "tutor": "46dfe3ef-e568-4916-a2e6-a4c9fb24a0df",
      "tutorOrgManager": "9260c46c-2ffd-4a42-a7a7-a4067f537f94"
  },
  {
      "uid": "71843fd7-a91b-40d7-9521-983af009c2d4",
      "first_name": "Amanda",
      "last_name": "George",
      "email_address": "ybruce@example.net",
      "phone_number": "001-300-248-9451",
      "student": null,
      "tutor": "bcbacec8-4e19-4f1b-993f-7abeb106147b",
      "tutorOrgManager": "269d2c4f-00d3-437d-a2d8-1c2321a558d6"
  },
  {
      "uid": "3cfdec86-6539-4bc3-b99b-b56143c79d0b",
      "first_name": "Trevor",
      "last_name": "Green",
      "email_address": "kendra66@example.org",
      "phone_number": "(234)500-7627",
      "student": null,
      "tutor": "05288a80-b8d2-480b-a6b3-fa93a73a1a40",
      "tutorOrgManager": "197c8bd0-1cf5-4333-957b-08ad9cf77b38"
  },
  {
      "uid": "9a9132d2-f3ec-4815-ba6a-8c21cf7b22c1",
      "first_name": "Pamela",
      "last_name": "Guzman",
      "email_address": "nunezedward@example.com",
      "phone_number": "(097)670-1720x09925",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "2252096f-f70a-469f-a52c-cd3e0d3a939d",
      "first_name": "Daniel",
      "last_name": "Dunn",
      "email_address": "james71@example.org",
      "phone_number": "+1-795-194-2641x830",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null
  },
  {
      "uid": "73312c33-5620-4fd9-af65-4ee863be9191",
      "first_name": "Kimberly",
      "last_name": "Wallace",
      "email_address": "stanleyclarke@example.org",
      "phone_number": "0740899331",
      "student": null,
      "tutor": "e6dae9eb-d13e-4c73-ab03-192189eb5a15",
      "tutorOrgManager": "3059a91b-924d-4dae-aa09-45663863aa11"
  },
  {
      "uid": "e261aa9f-06dc-46bb-b29c-a12fb26d864a",
      "first_name": "Kimberly",
      "last_name": "Wilkerson",
      "email_address": "hhunter@example.org",
      "phone_number": "(961)161-1620x76607",
      "student": "3caff8eb-2f47-4537-af85-62e2bf47caf7",
      "tutor": "1385cc5c-ea03-4d23-9b08-671c2febce90",
      "tutorOrgManager": "9f591444-c27e-455c-a42f-585b780b1830"
  },
  {
      "uid": "f0430d96-7e9e-4973-b802-98b76bff825a",
      "first_name": "Jennifer",
      "last_name": "Miller",
      "email_address": "martinezheather@example.com",
      "phone_number": "(203)519-2303x104",
      "student": "8639bc11-4672-4227-b8d1-18056433f2f2",
      "tutor": null,
      "tutorOrgManager": "13f5ce6f-b053-405e-bad7-f7fd57afcb8c"
  }
]

export const userMap = new Map<string, User>(userData.map(
  (user) => [user.uid, new User(
    user.uid,
    user.first_name,
    user.last_name,
    user.email_address,
    user.phone_number,
    studentMap.get(user.student),
    tutorMap.get(user.tutor), 
    tutorOrgManagerMap.get(user.tutorOrgManager)
  )] 
))

export const userArray:User[] = Array.from(userMap.values());

export const userArrayByTutor = userArray.filter((user)=>{
  return user.tutor ? true : false;
})

export const userArrayByStudent = userArray.filter((user)=>{
  return user.student ? true : false;
})

export const userArrayByTutorOrgManager = userArray.filter((user)=>{
  return user.tutorOrgManager ? true : false;
})

export const userMapByTutor = new Map<string, User>(userArrayByTutor.map((user)=>[user.tutor.tutorID, user]));
export const userMapByStudent = new Map<string, User>(userArrayByStudent.map((user)=>[user.student.studentId, user]));
export const userMapByTutorOrgManager = new Map<string, User>(userArrayByTutorOrgManager.map((user)=>[user.tutorOrgManager.tutorOrgManagerID, user]));