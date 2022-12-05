import {Student, Tutor, Class} from './index';


export default class Session {

  private _sessionId: string;
  private _tutors: Tutor[];
  private _students: Student[];
  private _classes: Class[];
  private _capacity: number;
  private _title: string;
  private _startTime: Date;
  private _endTime: Date;
  

  constructor(
    sessionId?: string,
    tutors?: Tutor[],
    students?: Student[],
    capacity?: number,
    title?: string,
    startTime?: Date,
    endTime?: Date,
    classes?: Class[]
  ){
    this._sessionId = sessionId;
    this._tutors = tutors;
    this._students = students;
    this._capacity = capacity;
    this._title = title;
    this._startTime = startTime;
    this._endTime = endTime;
    this._classes = classes;
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
  public get capacity(){
    return this._capacity;
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
  public get classes(){
    return this._classes;
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
  public set capacity(capacity: number){
    this._capacity = capacity;
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
  public set classes(classes: Class[]){
    this._classes = classes;
  }
 

}