import React from 'react'
import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect, useState } from 'react'
import colombia from '../../data/Colombia.json'

const colombiaflag = 'colombiaflag.png'
const colombiaflagPath = `/static/${colombiaflag}`

function Location({updateUserInfo}) {

  const[depId, setDepId] = useState('');
  const[depart, setDepart] = useState('');
  const[cities, setCities] = useState([]);
  const[city, setCity] = useState('');

  useEffect(()=>{
    AOS.init();
  },[])

  const departamentoSelect =(e)=>{
    const deparId = parseInt(e.target.value);
    const selectData = colombia.find(departamento => departamento.id == deparId);
    setDepart(selectData.departamento);
    setCities(selectData.ciudades);
    updateUserInfo({ userLocation: { departamento: selectData.departamento, municipio: '' } });
  }

  const ciudadSelect = (e)=>{
    const citySelect = e.target.value;
    setCity(citySelect);
    updateUserInfo({ userLocation: { departamento: depart, municipio: citySelect} });

  }


  return (
    <div data-aos="fade-left">
      <h2 style={{marginBottom:"20px"}}>Select the location where you want to live.</h2>
      <div className="country-section">
          <img src={colombiaflagPath} alt="colombia-flag" />
          <p>We're just in Colombia right now!</p>
      </div>
      <div className="location-selection">
        <label htmlFor="departamento">Departamento</label>
        <select name="Departamento" id="departamento" onChange={(e)=>departamentoSelect(e)}>
          <option value="">Select</option>
          {
            colombia.map((getDepartamento, index)=>(
              <option value={getDepartamento.id} key={index}>{getDepartamento.departamento}</option>
            ))
          }
        </select>
        <label htmlFor="municipio">Municipio</label>
        <select name="Departamento" id="departamento" onChange={(e)=>ciudadSelect(e)}>
          <option value="">Select</option>
          {
            cities.map((getCity, index)=>(
              <option key={index}>{getCity}</option>
            ))
          }
        </select>
      </div>
    </div>
  )
}

export default Location