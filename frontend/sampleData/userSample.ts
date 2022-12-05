import { tutorMap } from "./tutorSample"
import { studentMap } from "./studentSample"
import { tutorOrgManagerMap } from "./tutorOrgManagerSample"
import {User, Student, Tutor, TutorOrgManager} from "../classes"
const userData = [
  {
      "uid": "e3e70682-c209-4cac-a29f-6fbed82c07cd",
      "first_name": "Robert",
      "last_name": "Green",
      "email_address": "ysullivan@example.com",
      "phone_number": "593.824.2194x8924",
      "student": null,
      "tutor": "e61a441c-12e0-48b2-bad6-40fb19488dec",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "78de5857-5487-4e1e-af19-922ad9b8a714",
      "first_name": "Anita",
      "last_name": "Gomez",
      "email_address": "cheryl38@example.com",
      "phone_number": "840.801.6097x535",
      "student": null,
      "tutor": "30e9c5cc-101f-4ccc-9ed7-33e8b421eaeb",
      "tutorOrgManager": "3d15eef7-38c1-462e-9148-624feac1c14f",
      "password": "J=genius"
  },
  {
      "uid": "cd9d2b7d-247a-4333-b7b0-b7d2cda8056c",
      "first_name": "Amy",
      "last_name": "Davis",
      "email_address": "nancy71@example.com",
      "phone_number": "+1-418-583-9894",
      "student": "3dfabc08-935d-4d72-9129-fb7c6288e1a5",
      "tutor": "cc457821-98a6-416d-9775-336d71eacd05",
      "tutorOrgManager": "2fcd81b5-d24b-4ce4-b07b-f3262f120554",
      "password": "J=genius"
  },
  {
      "uid": "a81ad477-fb36-45b8-9cde-b3e60870e15c",
      "first_name": "Jordan",
      "last_name": "Jones",
      "email_address": "nancymclean@example.org",
      "phone_number": "001-868-483-3969x477",
      "student": null,
      "tutor": "b341facd-ff0a-40f1-a425-799aa905d750",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "5b7c709a-cb17-4a5a-bb82-860deabca8d0",
      "first_name": "Christopher",
      "last_name": "Salazar",
      "email_address": "vmatthews@example.org",
      "phone_number": "041.352.5601",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "b29a8b06-daf6-4c5f-a577-bffac87a7463",
      "password": "J=genius"
  },
  {
      "uid": "92e8e269-d12e-4bc4-8b94-75b138018b47",
      "first_name": "Cynthia",
      "last_name": "Zuniga",
      "email_address": "johnsoncynthia@example.net",
      "phone_number": "001-161-510-9032",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "35e8579a-7aaf-4e89-9fb7-97fab7d6467b",
      "password": "J=genius"
  },
  {
      "uid": "efdd35f8-0fa3-4266-8cfd-ba9bba26d851",
      "first_name": "Erin",
      "last_name": "Stephens",
      "email_address": "huffchad@example.org",
      "phone_number": "+1-456-208-7091x6345",
      "student": null,
      "tutor": "d69c91c2-7860-4602-bb4a-06cbe786ab37",
      "tutorOrgManager": "2b5f6932-91dc-49ef-ab21-a3f6e6fd68e8",
      "password": "J=genius"
  },
  {
      "uid": "f76fbfb8-3412-4c12-ac32-2c12b29c467d",
      "first_name": "Katrina",
      "last_name": "Kramer",
      "email_address": "meganpeterson@example.com",
      "phone_number": "972-076-9845",
      "student": "403d1f83-a859-490c-9670-f668637e0edc",
      "tutor": null,
      "tutorOrgManager": "753c7c99-032f-46ca-b0d9-c2aa8f837ef7",
      "password": "J=genius"
  },
  {
      "uid": "bd30291a-55fe-408e-943e-2e04bdd7d19b",
      "first_name": "Brandon",
      "last_name": "Campbell",
      "email_address": "kathleenolson@example.net",
      "phone_number": "599-246-6109x3523",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "60ef1471-72b8-4f39-a32c-9b6f391cf046",
      "first_name": "Jennifer",
      "last_name": "Nunez",
      "email_address": "sjohnson@example.net",
      "phone_number": "(027)142-7878x90075",
      "student": "0cc36d8c-7786-4fe5-9675-ebf74fe30c9a",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "f689a4a5-ffda-4336-8c6e-90373020da5c",
      "first_name": "Cynthia",
      "last_name": "Miller",
      "email_address": "valeriemorales@example.net",
      "phone_number": "(503)008-9131x93442",
      "student": "0597aab6-14d3-4dbc-a0ac-f4c9658de17e",
      "tutor": "ec3aa314-da9b-4017-b9c1-47c719a5711b",
      "tutorOrgManager": "cad6e514-ccc1-4d51-b3f6-60d8e9f41cc0",
      "password": "J=genius"
  },
  {
      "uid": "2227d96d-41a9-4f90-9c82-15271da3b7e2",
      "first_name": "Desiree",
      "last_name": "Roth",
      "email_address": "darin24@example.org",
      "phone_number": "0348559097",
      "student": null,
      "tutor": "756b0715-e718-4322-a4e6-95c9b65d1226",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "df14c612-5f58-45b5-af79-0959a3e04b3b",
      "first_name": "Amanda",
      "last_name": "Clark",
      "email_address": "alan24@example.com",
      "phone_number": "515-900-4229x45682",
      "student": "4ed13553-0c5a-476f-af0a-81ed3d5d60bc",
      "tutor": "bb0378eb-7a62-422e-9d69-d9fc4b1cb8bd",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "122411e6-ba89-42dd-85e6-9ea9db66bfda",
      "first_name": "Kevin",
      "last_name": "Houston",
      "email_address": "robert18@example.com",
      "phone_number": "551.717.6045x2296",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "a38d8afc-fdd2-4d7a-b97c-cc57ce5dc807",
      "password": "J=genius"
  },
  {
      "uid": "15ace7a1-ceca-4ee3-90da-8a9516408169",
      "first_name": "James",
      "last_name": "Walker",
      "email_address": "zsmith@example.net",
      "phone_number": "477.936.1534x92635",
      "student": "e72bb5b7-0712-4911-b3b6-8b57da54f267",
      "tutor": "dd138266-d26d-4396-9058-fe8c1d7173e5",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "33a1d1c2-ad4a-4155-809f-cd8f739cd488",
      "first_name": "David",
      "last_name": "Sanders",
      "email_address": "danielleshea@example.org",
      "phone_number": "+1-213-765-8219x729",
      "student": null,
      "tutor": "6c596216-ae0f-4bc8-a36b-cb0167e98363",
      "tutorOrgManager": "ade7cef3-7ed2-4c2f-856f-3d95e0ae1a1b",
      "password": "J=genius"
  },
  {
      "uid": "d5627386-528c-4241-a345-ac72eac39204",
      "first_name": "Vernon",
      "last_name": "Jimenez",
      "email_address": "amyvelazquez@example.org",
      "phone_number": "550-824-9269x47118",
      "student": "10fc9eee-0a17-47f7-aa5f-24b6de6fec4b",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "03e9ba02-4cea-4df0-8a66-dc4e21681081",
      "first_name": "Katherine",
      "last_name": "West",
      "email_address": "laurenmelton@example.com",
      "phone_number": "(868)809-1891x634",
      "student": "d872298c-7b72-490b-b8f8-f071d360da69",
      "tutor": "6af79ad2-993e-48c6-a6b1-06e289110af0",
      "tutorOrgManager": "d9efe28b-3bcb-40b3-961d-8dcf9b8086da",
      "password": "J=genius"
  },
  {
      "uid": "a83023ab-053e-4b42-8c4d-a021dd620222",
      "first_name": "Nicole",
      "last_name": "Yang",
      "email_address": "william45@example.org",
      "phone_number": "446.660.2234x5007",
      "student": "e3d48408-7de8-4234-a412-579d6af944e0",
      "tutor": null,
      "tutorOrgManager": "b2ddc481-ac6d-4df8-94e5-064cb799ae8e",
      "password": "J=genius"
  },
  {
      "uid": "5a4f4145-fc98-4279-8f6f-111c26c06e67",
      "first_name": "Robert",
      "last_name": "Carr",
      "email_address": "gellis@example.com",
      "phone_number": "001-200-992-5185x36710",
      "student": "a6855857-567e-4862-af15-1673a1df3da7",
      "tutor": "9d44c93e-7799-48e2-b368-c5539c30ceaa",
      "tutorOrgManager": "9f3dd894-b6af-48b2-aeba-42d0f8303249",
      "password": "J=genius"
  },
  {
      "uid": "208a393e-d960-4f85-89df-7e444bdffa7d",
      "first_name": "Susan",
      "last_name": "Hughes",
      "email_address": "sabrina18@example.org",
      "phone_number": "6753751007",
      "student": "f1dd50bf-06d2-4d7c-a6ac-9d8a4160ff92",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "e0397e67-9261-46de-91ba-cf80aaa07996",
      "first_name": "Jason",
      "last_name": "Davis",
      "email_address": "hhunter@example.org",
      "phone_number": "(961)161-1620x76607",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "53125ffd-f655-460b-9d32-e231eb561699",
      "first_name": "Jennifer",
      "last_name": "Miller",
      "email_address": "martinezheather@example.com",
      "phone_number": "(203)519-2303x104",
      "student": "2452bc39-dbf2-4ed1-bb9c-ea959ad7558f",
      "tutor": "eecb325b-064f-468d-b080-e0035e7f503c",
      "tutorOrgManager": "582dd972-7a08-4ca8-9cc5-a8a0743c7e9d",
      "password": "J=genius"
  },
  {
      "uid": "215203c7-421a-415e-b58c-43ceb51d70d8",
      "first_name": "Anthony",
      "last_name": "Clark",
      "email_address": "thomas44@example.net",
      "phone_number": "+1-529-118-9426x2235",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "c13e66af-3c95-40d3-be2a-ad3e82221345",
      "password": "J=genius"
  },
  {
      "uid": "6b770df1-5f59-4a2c-8a82-e06a2f16fb50",
      "first_name": "Elizabeth",
      "last_name": "Callahan",
      "email_address": "longjacqueline@example.org",
      "phone_number": "(486)296-4513x75806",
      "student": "f642c8f3-6acf-49eb-8228-4fd9689bba65",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "3438b4e4-70f8-4d99-9217-7eb7e6b920da",
      "first_name": "Nathan",
      "last_name": "Farley",
      "email_address": "clementslaura@example.com",
      "phone_number": "892-762-6623",
      "student": "766229cc-5af9-4c78-a47f-4d9785fa2d5c",
      "tutor": "efe6171b-5723-4959-b415-1accf5a3e893",
      "tutorOrgManager": "c149fa8e-7bb8-42f1-9624-d318a32652e8",
      "password": "J=genius"
  },
  {
      "uid": "d4864482-0078-4b12-8b73-50d13421beaf",
      "first_name": "Holly",
      "last_name": "Montgomery",
      "email_address": "robinsondanny@example.net",
      "phone_number": "892-671-7386x4014",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "00109824-0a61-4be3-ab22-12c9e23b580e",
      "password": "J=genius"
  },
  {
      "uid": "e3fbdbda-86ae-4d5c-a5ff-6adc41aef3f7",
      "first_name": "Bonnie",
      "last_name": "Foster",
      "email_address": "francismichael@example.net",
      "phone_number": "910.144.8518",
      "student": "eb83af16-e404-4808-bfc1-8c00dc0520a4",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "4a294067-dc66-427b-aa32-5333116e8a64",
      "first_name": "Justin",
      "last_name": "Taylor",
      "email_address": "amandajenkins@example.net",
      "phone_number": "+1-644-759-2211",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "77cb1a27-974f-4edc-a6b6-208761a53fdd",
      "password": "J=genius"
  },
  {
      "uid": "4c88b9d8-ab12-4b53-8f42-cebe23b870f3",
      "first_name": "Michael",
      "last_name": "Kennedy",
      "email_address": "frobinson@example.net",
      "phone_number": "570.742.7093x05760",
      "student": "11035083-fa99-4f9b-86de-3365d8a230de",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "f305ee95-afb1-40f4-94d4-dad6ddfae808",
      "first_name": "Judy",
      "last_name": "Caldwell",
      "email_address": "warddarren@example.org",
      "phone_number": "432-943-1675x625",
      "student": null,
      "tutor": "affe2554-e5ae-4699-a5e3-a7196bf52dfd",
      "tutorOrgManager": "eee84bcb-7281-48a9-a5e4-979d6f6ddf79",
      "password": "J=genius"
  },
  {
      "uid": "50ea1324-862f-48e1-a5c2-9b6ab575bc6e",
      "first_name": "David",
      "last_name": "Lozano",
      "email_address": "ybailey@example.com",
      "phone_number": "633.739.0603x1250",
      "student": "2c623ac3-ad70-47cf-a358-cb1dbe3feafd",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "162d5c72-9ccd-4e1f-8c2a-bdaa9c5c11eb",
      "first_name": "Janet",
      "last_name": "Hunt",
      "email_address": "kelsey56@example.com",
      "phone_number": "8869774735",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "0d742256-0b36-43cd-8acf-eba4441030ae",
      "first_name": "Francisco",
      "last_name": "Smith",
      "email_address": "taylorkristin@example.net",
      "phone_number": "968.373.5919",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "51abf5e5-cb77-4e24-95eb-3a3de2014a45",
      "first_name": "Marcus",
      "last_name": "Bryant",
      "email_address": "jonathan80@example.org",
      "phone_number": "(138)533-4448x647",
      "student": "8d4e2753-ef26-45b7-8e49-df560b648acd",
      "tutor": "3d6e2667-b665-4d6e-9f39-ccaa580c79fc",
      "tutorOrgManager": "b97fb3bb-7ecc-440c-b5ff-93f0025b7c5f",
      "password": "J=genius"
  },
  {
      "uid": "cf1accc1-eaca-4811-8c26-e5d9702dc88a",
      "first_name": "Robert",
      "last_name": "Snyder",
      "email_address": "fwilson@example.org",
      "phone_number": "263-791-6860",
      "student": "deffed7a-d728-4256-a0ca-35ab38553ac8",
      "tutor": "7d718591-3fee-4fc7-ae2d-ffdff57b8a92",
      "tutorOrgManager": "fea2a33a-51d1-4bcd-9a23-754bef38d426",
      "password": "J=genius"
  },
  {
      "uid": "e64ddd91-8e9b-485e-9b77-0deb6f51ea78",
      "first_name": "Justin",
      "last_name": "Weaver",
      "email_address": "jenniferwaters@example.net",
      "phone_number": "+1-784-430-1912x633",
      "student": null,
      "tutor": "ff4533fe-bc6f-46ac-a139-d15d48d8b9ef",
      "tutorOrgManager": "89181ba3-bdee-4231-81a6-009ea8dce886",
      "password": "J=genius"
  },
  {
      "uid": "0cbdc014-dbed-442e-ada3-13e783e9973b",
      "first_name": "David",
      "last_name": "Brewer",
      "email_address": "maddoxannette@example.org",
      "phone_number": "+1-843-318-4535x74922",
      "student": "a2834536-95de-4d6e-9df2-e07353f04099",
      "tutor": "813dd49a-8d99-443c-83f7-ba05cf4bb315",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "6544c97d-e078-4f97-a13c-121ccfdef303",
      "first_name": "Eric",
      "last_name": "Thompson",
      "email_address": "taylorjamie@example.com",
      "phone_number": "001-332-365-9927",
      "student": "989bb030-86c4-4b06-86a8-e22fd57caf0d",
      "tutor": "9db3466d-1ba6-4c61-aaf9-4919e69b7971",
      "tutorOrgManager": "033c1469-4f06-4a18-b4a2-64447d3c279b",
      "password": "J=genius"
  },
  {
      "uid": "a71b80ef-8e36-482f-b856-be31f568c9c6",
      "first_name": "Frank",
      "last_name": "Koch",
      "email_address": "tpayne@example.org",
      "phone_number": "296-354-6030x535",
      "student": null,
      "tutor": "b9cde60c-ab1e-4794-b0f2-297adceb2013",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "42965873-39d5-4552-a867-a0f0a8e6a772",
      "first_name": "Max",
      "last_name": "Martin",
      "email_address": "kellyamber@example.net",
      "phone_number": "+1-250-700-3003x5105",
      "student": null,
      "tutor": "22c71d04-6c32-4aff-a9fa-4ea6f8db1a4d",
      "tutorOrgManager": "72ef7dce-376e-42a6-ac07-1cf1e47638ec",
      "password": "J=genius"
  },
  {
      "uid": "4fdc1351-5ba8-40dc-a45d-b6ca6f6a2196",
      "first_name": "Gregory",
      "last_name": "Murphy",
      "email_address": "areyes@example.com",
      "phone_number": "+1-870-916-6208",
      "student": null,
      "tutor": "a9774b71-de6d-4d7e-9f31-2acb2362dbc1",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "b3191702-bb80-498d-970d-a545839137a6",
      "first_name": "Eddie",
      "last_name": "Rivera",
      "email_address": "johnjohnson@example.org",
      "phone_number": "001-821-691-9729x9045",
      "student": "606375b8-bb93-4826-bcee-9d29ce4f1ca0",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "094c0230-e3b4-4f81-aeb3-462ca032149d",
      "first_name": "Tyler",
      "last_name": "Howard",
      "email_address": "stephenromero@example.org",
      "phone_number": "001-654-760-4848x7089",
      "student": "afd4fc7b-ef20-4346-832f-b3088d56206d",
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "1eb95739-b8ac-4d81-a522-ff4674b7061c",
      "first_name": "Richard",
      "last_name": "Crawford",
      "email_address": "nelsonwendy@example.com",
      "phone_number": "+1-943-885-6431x95398",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "299cf16b-5a75-43c0-a02a-35e9ae6b4c8e",
      "first_name": "Sabrina",
      "last_name": "Lam",
      "email_address": "meghan09@example.org",
      "phone_number": "001-255-445-7696",
      "student": "c9d0a7f4-0042-4fc6-ab87-71dffccae6b8",
      "tutor": null,
      "tutorOrgManager": "20379089-711f-410a-8b29-75c6918ff358",
      "password": "J=genius"
  },
  {
      "uid": "f2d7fe55-0262-45aa-adec-31ef57627626",
      "first_name": "Jennifer",
      "last_name": "Browning",
      "email_address": "julie31@example.net",
      "phone_number": "(428)212-9188x96644",
      "student": null,
      "tutor": "c74dd25c-6dbf-459c-837d-975248f3531c",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "47caf779-b7c9-4da8-91db-32f8fda834ea",
      "first_name": "Sophia",
      "last_name": "Medina",
      "email_address": "veronica36@example.org",
      "phone_number": "8296570869",
      "student": "8772c347-5cba-4be3-8404-64c0e65a3ae4",
      "tutor": "3a72017d-c29e-4120-8ddb-2316cc68fd3f",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "5abec113-a183-4fdb-b1cb-5e8eae2562ca",
      "first_name": "Courtney",
      "last_name": "Crawford",
      "email_address": "ashleyallen@example.org",
      "phone_number": "001-619-737-8132x71664",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "c1fa924e-e1bc-4fb2-afed-6cc540b000a4",
      "first_name": "Kiara",
      "last_name": "Lynch",
      "email_address": "parkertravis@example.com",
      "phone_number": "666.609.7592",
      "student": "79460978-65e9-4753-8638-9bd3d26eeeba",
      "tutor": "53ff6644-4741-4e56-b5e2-834d907d8532",
      "tutorOrgManager": "90e0172f-14dc-41bc-8aa5-658322a5a421",
      "password": "J=genius"
  },
  {
      "uid": "01267789-5c6b-4596-98f1-6c91dd6d47e4",
      "first_name": "Chad",
      "last_name": "Love",
      "email_address": "bwilliams@example.com",
      "phone_number": "(246)292-6480x2227",
      "student": "c399fd7f-b75d-471e-a453-1fe9b48f653e",
      "tutor": null,
      "tutorOrgManager": "85050a17-d2e1-4d4d-bad4-c2880bf56ed8",
      "password": "J=genius"
  },
  {
      "uid": "b0f1bb1d-8e10-4ed6-92d0-72230b20ee0f",
      "first_name": "Julie",
      "last_name": "Welch",
      "email_address": "melvinwillis@example.org",
      "phone_number": "824-345-4487",
      "student": null,
      "tutor": "c1b5468a-27bb-4580-a8f5-8c5dffa08419",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "271f2772-8d7f-4ba5-b2e6-316ee6710ad2",
      "first_name": "Benjamin",
      "last_name": "Richards",
      "email_address": "huangleslie@example.org",
      "phone_number": "793.782.5278",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "d21276c2-1519-401c-8b1f-11370ea255e0",
      "first_name": "Zachary",
      "last_name": "Smith",
      "email_address": "garciacathy@example.net",
      "phone_number": "568.512.5022x059",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "a5387901-69f1-4ccd-8b4c-ba0a317eeb1d",
      "password": "J=genius"
  },
  {
      "uid": "cbf8e26a-4fae-467b-b2e7-4e770fe1cedf",
      "first_name": "Perry",
      "last_name": "Williams",
      "email_address": "michaelconley@example.org",
      "phone_number": "(075)994-4976x20743",
      "student": "59cd012a-06b4-4b6f-9f94-e3c818a77594",
      "tutor": "5b8c4949-1068-41d3-a33d-9c54f30459cc",
      "tutorOrgManager": "b0c952af-9db3-4510-a75d-08552d5590c9",
      "password": "J=genius"
  },
  {
      "uid": "52a33c33-037e-4725-a5a1-bdaea747795e",
      "first_name": "Stephen",
      "last_name": "Spencer",
      "email_address": "dalvarez@example.net",
      "phone_number": "(408)115-5170x2840",
      "student": "259a2b28-b22b-4974-8c5c-192ff1c51dda",
      "tutor": "28280370-5672-4bc7-a06e-8502002f9cc4",
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "28b299bc-ebbe-4a41-8781-e11f2cb38568",
      "first_name": "Danielle",
      "last_name": "Sanchez",
      "email_address": "sonya76@example.org",
      "phone_number": "345.235.3267",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "2353d455-90bc-4b66-a063-14505d005716",
      "password": "J=genius"
  },
  {
      "uid": "03729e33-c550-4d2b-909e-7f7862f25291",
      "first_name": "Fernando",
      "last_name": "Silva",
      "email_address": "lhiggins@example.org",
      "phone_number": "0580001992",
      "student": null,
      "tutor": null,
      "tutorOrgManager": "c96ef1a5-ac70-4464-a734-f9bbc7405255",
      "password": "J=genius"
  },
  {
      "uid": "6b325d48-06c4-4109-89a6-e611613f718d",
      "first_name": "Samuel",
      "last_name": "Mcintyre",
      "email_address": "jennifer25@example.net",
      "phone_number": "861.269.5166",
      "student": null,
      "tutor": null,
      "tutorOrgManager": null,
      "password": "J=genius"
  },
  {
      "uid": "399bcb79-61ba-4a39-b89c-3c723ee29e68",
      "first_name": "Sabrina",
      "last_name": "Allen",
      "email_address": "lsanders@example.org",
      "phone_number": "485-809-9734x095",
      "student": "e0acf9ff-88d3-481a-9b4e-1428a0483bb2",
      "tutor": "f6d080c4-6409-4f32-8c4e-66dade0989b9",
      "tutorOrgManager": null,
      "password": "J=genius"
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
console.log(userArray);
export const userArrayByTutor = userArray.filter((user)=>{
  return user.getTutor() ? true : false;
})
console.log(userArrayByTutor)
export const userArrayByStudent = userArray.filter((user)=>{
  return user.getStudent() ? true : false;
})

export const userArrayByTutorOrgManager = userArray.filter((user)=>{
  return user.getTutorOrgManager() ? true : false;
})

export const userMapByTutor = new Map<string, User>(userArrayByTutor.map((user)=>[user.getTutor().tutorID, user]));
export const userMapByStudent = new Map<string, User>(userArrayByStudent.map((user)=>[user.getStudent().studentID, user]));
export const userMapByTutorOrgManager = new Map<string, User>(userArrayByTutorOrgManager.map((user)=>[user.getTutorOrgManager().tutorOrgManagerID, user]));