import { Session } from "../classes"
import {tutorMap, tutorOrgManagerMap, studentMap, userMap, tutorArray, userArray, tutorOrgManagerArray, studentArray} from './';
const sampleSessions:Session[] = [
  new Session(
    "0",
    tutorArray.slice(0, 3),
    studentArray.slice(3, 9),
    "Test Session 0",
    new Date(Date.now()),
    new Date(Date.now()+86400)
  )
]