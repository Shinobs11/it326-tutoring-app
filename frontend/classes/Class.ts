


export default class Class{

  private _classId: string;
  private _className: string;
  private _classDescription?: string;


  constructor(
    classId: string,
    className: string,
    classDescription?: string
  ){
    this._classId = classId;
    this._className = className;
    this._classDescription = classDescription;
  }


  public get classId(){
    return this._classId;
  }
  public get className(){
    return this._className;
  }
  public get classDescription(){
    return this._classDescription;
  }

  public set classId(classId: string){
    this._classId = classId;
  }
  public set className(className: string){
    this._className = className;
  }
  public set classDescription(classDescription: string){
    this._classDescription = classDescription;
  }
  






}














