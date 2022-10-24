
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
  
  createTutorOrganization(): TutorOrganization{
    console.log("createTutorOrganization");
    return{};
  }
  createTutorSession(tutorOrg: TutorOrganization): TutorSession{
    console.log("createTutorSession");
    return{};
  }


}