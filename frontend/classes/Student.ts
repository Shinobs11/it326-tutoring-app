

interface TutorSession{} //dummy interface

export default class Student{
  private _schoolYear: number;
  private _tutorSessionHours: number; //TODOS: What does this mean?

  constructor(
    schoolYear: number,
    tutorSessionHours: number
  ){
    this._schoolYear = schoolYear;
    this._tutorSessionHours = tutorSessionHours;
  }

  public get schoolYear(){
    return this._schoolYear;
  }
  public get tutorSessionHours(){
    return this._tutorSessionHours;
  }

  public set schoolYear(schoolYear: number){
    this._schoolYear = schoolYear;
  }
  public set tutorSessionHours(tutorSessionHours: number){
    this._tutorSessionHours = tutorSessionHours;
  }

  rateTutorSession(tutorSession: TutorSession){
    console.log("rateTutorSession");
  }
  attendSession(tutorSession: TutorSession){
    console.log("attendSession");
  }
}





