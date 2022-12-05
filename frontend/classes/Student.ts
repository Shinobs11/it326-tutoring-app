

interface TutorSession{} //dummy interface

export default class Student{
  private _studentID: string;
  private _yearInSchool: number;

  constructor(
    studentID: string,
    yearInSchool: number,
  ){
    this._studentID = studentID;
    this._yearInSchool = yearInSchool;
  }


  public get studentID(){
    return this._studentID;
  }

  public get yearInSchool(){
    return this._yearInSchool;
  }

  public set studentID(studentID: string){
    this._studentID = studentID;
  }

  public set yearInSchool(yearInSchool: number){
    this._yearInSchool = yearInSchool;
  }


  rateTutorSession(tutorSession: TutorSession){
    console.log("rateTutorSession");
  }
  attendSession(tutorSession: TutorSession){
    console.log("attendSession");
  }
}





