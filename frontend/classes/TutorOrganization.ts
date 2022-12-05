import User from "./User";


export default class TutorOrganization {

  private _orgID: number;
  private _name: string;
  private _description: string;
  private _tutors: User[];
  private _managers: User[];




  constructor(orgID: number, name: string, description: string, tutors: User[], managers: User[]) {
    this._orgID = orgID;
    this._name = name;
    this._description = description;
    this._tutors = tutors;
    this._managers = managers;
  }

  get orgID(): number {
    return this._orgID;
  }

  set orgID(value: number) {
    this._orgID = value;
  }

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }

  get description(): string {
    return this._description;
  }

  set description(value: string) {
    this._description = value;
  }

  get tutors(): User[] {
    return this._tutors;
  }

  set tutors(value: User[]) {
    this._tutors = value;
  }

  get managers(): User[] {
    return this._managers;
  }

  set managers(value: User[]) {
    this._managers = value;
  }








}