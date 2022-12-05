
interface TutorSession{} //dummy interface
interface TutorOrganization{} //dummy interface

export default class TutorOrgManager{
  private _tutorOrgManagerID: string;

  constructor(
    tutorOrgManagerID: string
  ){
    this._tutorOrgManagerID = tutorOrgManagerID;
  }

  public get tutorOrgManagerID(){
    return this._tutorOrgManagerID;
  }

  public set tutorOrgManagerID(tutorOrgManagerID: string){
    this._tutorOrgManagerID = tutorOrgManagerID;
  }
  



}