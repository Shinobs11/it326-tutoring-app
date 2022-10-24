import Tutor from "./Tutor";
import Student from "./Student";
import TutorOrgManager from "./TutorOrgManager";
export default class User{
  private _name: string;
  private _userID: string;
  private _password: string;
  private _phoneNo: string;
  private _email: string;
  private _tutor?: Tutor;
  private _student?: Student;
  private _tutorOrgManager?: TutorOrgManager;

  constructor(
    name: string,
    userID: string,
    password: string,
    phoneNo: string,
    email: string,
    tutor?: Tutor, // question mark means optional
    student?: Student,
    tutorOrgManager?: TutorOrgManager
  ){
    this._name = name;
    this._userID = userID;
    this._password = password;
    this._phoneNo = phoneNo;
    this._email = email;
    this._tutor = tutor;
    this._student = student;
    this._tutorOrgManager = tutorOrgManager;
  }

  public get name(){
    return this._name;
  }
  public get userID(){
    return this._userID;
  }
  public get password(){
    return this._password;
  }
  public get phoneNo(){
    return this._phoneNo;
  }
  public get email(){
    return this._email;
  }

  //TODOS: Figure out how to implement this using getters and setters
  // public get tutor(){
  //   return this._tutor;
  // }
  // public get student(){
  //   return this._student;
  // }
  // public get tutorOrgManager(){
  //   return this._tutorOrgManager;
  // }
  public getTutor(){
    return this._tutor;
  }
  public getStudent(){
    return this._student;
  }
  public getTutorOrgManager(){
    return this._tutorOrgManager;
  }
  




  public set name(name: string){
    this._name = name;
  }
  public set userID(userID: string){
    this._userID = userID;
  }
  public set password(password: string){
    this._password = password;
  }
  public set phoneNo(phoneNo: string){
    this._phoneNo = phoneNo;
  }
  public set email(email: string){
    this._email = email;
  }
  public set tutor(tutor: Tutor){
    this._tutor = tutor;
  }
  public set student(student: Student){
    this._student = student;
  }
  public set tutorOrgManager(tutorOrgManager: TutorOrgManager){
    this._tutorOrgManager = tutorOrgManager;
  }


  login(userID: string, password: string): void{
    console.log("login");
  }
  authenticate(): void{
    console.log("authenticate");
  }
}










