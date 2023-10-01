import React from 'react'
import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect, useState } from 'react'

function PInfo({updateUserInfo}) {

  const [Perinfo, setPerinfo] = useState({
    
    email: '',
    fullname: '',
    password: ''
  });


  const habdleInput = (e)=>{
    const {name, value} = e.target;
    setPerinfo((infoPrev)=>({
      ...infoPrev,
      [name]: value,
    }));

    //Test -- falta validación, para que obligatoriamente se completen los campos.
    updateUserInfo({personalInfo: Perinfo})

  }

  useEffect(()=>{
    AOS.init();
  },[])

  return (
    <div data-aos="fade-left">
      <div className='personal-info'>
        <label htmlFor="email">Email</label>
        <input type="email" name="email" id="email-sign" placeholder="Type your email" value={Perinfo.email} onChange={habdleInput}/>
        <label htmlFor="fname">Full Name</label>
        <input type="text" name="fullname" id="name-sign" placeholder="Type your full name" value={Perinfo.fullname} onChange={habdleInput}/>
        <label htmlFor="password">Password</label>
        <input type="password" name="password" id="passw-sign" placeholder="Type your password" value={Perinfo.password} onChange={habdleInput}/>
      </div>
    </div>
  )
}

export default PInfo