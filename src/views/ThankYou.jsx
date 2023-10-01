import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom';

function ThankYou() {

  const navigate = useNavigate();

  async function return202(){  //Esta función es un test para simular el estado de OK del backend, para así esperar los 2 segundos para que se redireccione a la página de inicio.
    await new Promise((resolve) => setTimeout(resolve, 2000));
    return 202;
  }

  
  useEffect(() => {
    async function getData(){
      const data = await return202();
      console.log(data)
      if (data === 202)
      {
        navigate("/home");
      }
    }
    getData();
  }, [])
  

  return (
    <>
    
    <div className='thankyou-container'>
      <h1>Thank you for signing up! You will be redirected in a few seconds...</h1>
    </div>
    
    </>
  )
}

export default ThankYou