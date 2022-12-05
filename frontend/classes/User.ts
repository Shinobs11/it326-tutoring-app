import Tutor from "./Tutor";
import Student from "./Student";
import TutorOrgManager from "./TutorOrgManager";
export default class User{
  private _first_name: string;
  private _last_name: string;
  private _uid: string;
  private _phone_number: string;
  private _email_address: string;
  private _tutor?: Tutor;
  private _student?: Student;
  private _tutorOrgManager?: TutorOrgManager;

  constructor(
    uid: string,
    first_name: string,
    last_name: string,
    email_address: string,
    phone_number: string,
    student?: Student,
    tutor?: Tutor, // question mark means optional
    tutorOrgManager?: TutorOrgManager
  ){
    this._uid = uid;
    this._first_name = first_name;
    this._last_name = last_name;
    this._email_address = email_address;
    this._phone_number = phone_number;
    this._student = student;
    this._tutor = tutor;
    this._tutorOrgManager = tutorOrgManager;
  }

  public get firstName(){
    return this._first_name;
  }
  public get lastName(){
    return this._last_name;
  }
  public get uid(){
    return this._uid;
  }

  public get phoneNumber(){
    return this._phone_number;
  }
  public get emailAddress(){
    return this._email_address;
  }
  public getStudent(){
    return this._student;
  }
  public getTutor(){
    return this._tutor;
  }
  public getTutorOrgManager(){
    return this._tutorOrgManager;
  }
  




  public set uid(uid: string){
    this._uid = uid;
  }
  public set phoneNo(phoneNo: string){
    this._phone_number = phoneNo;
  }
  public set email(email: string){
    this._email_address = email;
  }
  public set student(student: Student){
    this._student = student;
  }
  public set tutor(tutor: Tutor){
    this._tutor = tutor;
  }
  public set tutorOrgManager(tutorOrgManager: TutorOrgManager){
    this._tutorOrgManager = tutorOrgManager;
  }


}










