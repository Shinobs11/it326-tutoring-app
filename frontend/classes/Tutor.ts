export default class Tutor{
  private _tutorID: string; // TODOS: should be UUID type
  private _rating: number;
  private _tutorSubject: string;
  private _numOfTutorOrgs: number; // TODOS: seems like this should actually be a map object


  constructor(
    tutorID: string,
    rating?: number,
    tutorSubject?: string,
    numOfTutorOrgs?: number
  ){
    this._tutorID = tutorID;
    this._rating = rating;
    this._tutorSubject = tutorSubject;
    this._numOfTutorOrgs = numOfTutorOrgs;
  }

  static fromTutor(tutor: Tutor): Tutor{
    return new Tutor(
      tutor.tutorID,
      tutor.rating,
      tutor.tutorSubject,
      tutor.numOfTutorOrgs
    );
  }

  public get tutorID(){
    return this._tutorID;
  }
  public get rating(){
    return this._rating;
  }
  public get tutorSubject(){
    return this._tutorSubject;
  }
  public get numOfTutorOrgs(){
    return this._numOfTutorOrgs;
  }

  public set tutorID(tutorID: string){
    this._tutorID = tutorID;
  }
  public set rating(rating: number){
    this._rating = rating;
  }
  public set tutorSubject(tutorSubject: string){
    this._tutorSubject = tutorSubject;
  }
  public set numOfTutorOrgs(numOfTutorOrgs: number){
    this._numOfTutorOrgs = numOfTutorOrgs;
  }

}