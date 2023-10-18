import React from 'react'
import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect, useState } from 'react'

function PInfo({updateUserInfo}) {
  const [Perinfo, setPerinfo] = useState({
    email: '',
    name: '',
    lastname: '',
    password: '',
    age: '',
  });


  const habdleInput = (e)=>{
    const {name, value} = e.target;
    setPerinfo((infoPrev)=>({
      ...infoPrev,
      [name]: value,
    }));

    //Test -- falta validación, para que obligatoriamente se completen los campos.
    //updateUserInfo({personalInfo: Perinfo})

  }

  useEffect(()=>{
    AOS.init();
  },[])

  useEffect(() => {
    updateUserInfo({ personalInfo: Perinfo });
  }, [Perinfo, updateUserInfo]);


  return (
    <form method="POST" action="/signup/">
      <div data-aos="fade-left">
        <div className='personal-info'>
          <label htmlFor="email">Correo</label>
          <input type="email" name="email" required id="email-sign" placeholder="Escribe tu correo" value={Perinfo.email} onChange={habdleInput}/>
          <label htmlFor="password">Contraseña</label>
          <input type="password" name="password" required id="passw-sign" placeholder="Escribe tu contraseña" value={Perinfo.password} onChange={habdleInput}/>
          <label htmlFor="name">Nombre</label>
          <input type="text" name="name" required id="name-sign" placeholder="Escribe tu nombre" value={Perinfo.name} onChange={habdleInput}/>
          <label htmlFor="lastname">Apellido</label>
          <input type="text" name="lastname" required id="name-sign" placeholder="Escribe tu apellido" value={Perinfo.lastname} onChange={habdleInput}/>
          <label htmlFor="age">Edad</label>
          <input type="number" name="age" required id="name-sign" placeholder="Escribe tu edad" value={Perinfo.age} onChange={habdleInput}/>
        </div>
      </div>
    </form>
  )
}

export default PInfo