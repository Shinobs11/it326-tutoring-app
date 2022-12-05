import { Session } from "../classes"
import {tutorMap, tutorOrgManagerMap, studentMap, userMap, tutorArray, userArray, tutorOrgManagerArray, studentArray} from '.';
import getSample from '../utils/getSample'
import { classSample } from "./classes";
export const sessionSample:Session[] = [
  new Session(
    "0",
    tutorArray.slice(0, 3),
    studentArray.slice(3, 9),
    40,
    "Test Session 0",
    new Date(2022, 11, 29, 14, 30),
    new Date(2022, 11, 29, 15, 50),
    getSample(classSample, 3)
  ),
  new Session(
    "1",
    tutorArray.slice(0, 6),
    studentArray.slice(4, 10),
    20,
    "Test session 1",
    new Date(2022, 11, 30, 13, 30),
    new Date(2022, 11, 30, 14, 45),
    getSample(classSample, 2)
  ),
  new Session(
    "2",
    tutorArray.slice(6, 7),
    studentArray.slice(0, 4),
    10,
    "Test session 2",
    new Date(2022, 12, 3, 16, 30),
    new Date(2022, 12, 3, 18, 0),
    getSample(classSample, 1)
  )
]