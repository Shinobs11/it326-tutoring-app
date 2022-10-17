import React, { useState, useEffect } from 'react';



const ExampleComponent = () => {
  /**
    useState maintains "exampleState" between renders.
    when state is updated using "setExampleState", the component re-renders.
   */
  const [exampleState, setExampleState] = useState(null);

  useEffect(()=>{
    // do something on each render (generally not a good idea)
    return () =>{
      //do something on unmount OR before the next useEffect is called
    }
  })

  useEffect(() => {
    // Do something when component is mounted
    return ()=>{
      // Do something when component is unmounted OR before next useEffect is called
    }
  }, []);

  useEffect(()=>{
    // Do something when exampleState changes.
    return () =>{
      // Do something when component is unmounted OR before next useEffect is called
    }
  }, [exampleState])

  //React components return HTML and other React components
  return(
    <div>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae
      </p>
    </div>
  )

};

export default ExampleComponent;

