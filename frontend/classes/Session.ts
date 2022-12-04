import {Student, Tutor} from './index';


export default class Session {

  private _sessionId: string;
  private _tutors: Tutor[];
  private _students: Student[];
  private _title: string;
  private _startTime: Date;
  private _endTime: Date;
  

  constructor(
    sessionId?: string,
    tutors?: Tutor[],
    students?: Student[],
    title?: string,
    startTime?: Date,
    endTime?: Date
  ){
    this._sessionId = sessionId;
    this._tutors = tutors;
    this._students = students;
    this._title = title;
    this._startTime = startTime;
    this._endTime = endTime;
  }

  public get sessionId(){
    return this._sessionId;
  }
  public get tutors(){
    return this._tutors;
  }
  public get students(){
    return this._students;
  }
  public get title(){
    return this._title;
  }
  public get startTime(){
    return this._startTime;
  }
  public get endTime(){
    return this._endTime;
  }

  public set sessionId(sessionId: string){
    this._sessionId = sessionId;
  }
  public set tutors(tutors: Tutor[]){
    this._tutors = tutors;
  }
  public set students(students: Student[]){
    this._students = students;
  }
  public set title(title: string){
    this._title = title;
  }
  public set startTime(startTime: Date){
    this._startTime = startTime;
  }
  public set endTime(endTime: Date){
    this._endTime = endTime;
  }







}