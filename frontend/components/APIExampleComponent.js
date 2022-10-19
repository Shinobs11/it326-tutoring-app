import React, { useState, useEffect } from "react";

const apiURL = "http://127.0.0.1:8000/user/"; // URL for the API call
const ExampleRequest = new Request(apiURL, { // Request we're going to make to the django api
  method: "GET", //HTTP method used
  mode: "cors", //just keep it as cors
});

const APIExampleComponent = () => {
  const [loaded, setLoaded] = useState(false); // loading status
  const [users, setUsers] = useState(null); // user
  useEffect(() => {
    let getUsers = async ()=>{
      let response = await fetch(ExampleRequest);
      setUsers(await response.json());
      console.log(users);
      setLoaded(true);
    }
    getUsers();
  
  }, []);





  const UserComponent = ({uid, first_name, last_name, email, phone_number, ...props}) =>{
    return(
      <div>
        <h3>
          Primary key: {uid}
        </h3>
        <p>
          First Name: {first_name}
          Last Name: {last_name}
          Email: {email}
          Phone Number: {phone_number}
        </p>
      </div>
    )
  }



  if (loaded) {
    return <>{
      for(let user in )
    }</>;
  } else {
    return <></>;
  }
};

export default APIExampleComponent;



