import React from 'react'
import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect, useState } from 'react'

function PInfo({updateUserInfo}) {
  const [Perinfo, setPerinfo] = useState({
    email: '',
    password: '',
    nombre: '',
    apellido: '',
    edad: '',
  });

  const handleInput = (e)=>{
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
          <input type="email" name="email" id="email-sign" placeholder="Escribe tu correo" value={Perinfo.email} onChange={handleInput} />
          <label htmlFor="password">Contraseña</label>
          <input type="password" name="password" id="name-sign" placeholder="Escribe tu contraseña" value={Perinfo.password} onChange={handleInput} />
          <label htmlFor="nombre">Nombre</label>
          <input type="text" name="nombre" id="name-sign" placeholder="Escribe tu nombre" value={Perinfo.nombre} onChange={handleInput} />
          <label htmlFor="apellido">Apellido</label>
          <input type="text" name="apellido" id="name-sign" placeholder="Escribe tu apellido" value={Perinfo.apellido} onChange={handleInput} />
          <label htmlFor="edad">Edad</label>
          <input type="number" name="edad" id="name-sign" placeholder="Escribe tu edad" value={Perinfo.edad} onChange={handleInput} />
        </div>
      </div>
    </form>
      
  )
}

export default PInfo