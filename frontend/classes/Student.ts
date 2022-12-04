

interface TutorSession{} //dummy interface

export default class Student{
  private _studentId: string;
  private _yearInSchool: number;

  constructor(
    studentId: string,
    yearInSchool: number,
  ){
    this._studentId = studentId;
    this._yearInSchool = yearInSchool;
  }


  public get studentId(){
    return this._studentId;
  }

  public get yearInSchool(){
    return this._yearInSchool;
  }

  public set studentId(studentId: string){
    this._studentId = studentId;
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





