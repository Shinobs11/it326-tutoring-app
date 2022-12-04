import { Session } from "../classes"
import {tutorMap, tutorOrgManagerMap, studentMap, userMap, tutorArray, userArray, tutorOrgManagerArray, studentArray} from './';
export const sampleSessions:Session[] = [
  new Session(
    "0",
    tutorArray.slice(0, 3),
    studentArray.slice(3, 9),
    "Test Session 0",
    new Date(2022, 11, 29, 14, 30),
    new Date(2022, 11, 29, 15, 50)
  ),
  new Session(
    "1",
    tutorArray.slice(0, 6),
    studentArray.slice(4, 10),
    "Test session 1",
    new Date(2022, 11, 30, 13, 30),
    new Date(2022, 11, 30, 14, 45)
  ),
  new Session(
    "2",
    tutorArray.slice(6, 7),
    studentArray.slice(0, 4),
    "Test session 2",
    new Date(2022, 12, 3, 16, 30),
    new Date(2022, 12, 3, 18, 0)
  )
]