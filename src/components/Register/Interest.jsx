import React from 'react'
import InterestCard from '../InterestCard/InterestCard'
import Interests from '../../data/Interests.json'
import { useState } from 'react';

function Interest({updateUserInfo}) {


  const[siInterest, setSInterest] = useState([]);

  const handleInterest = (interestName) =>{
      setSInterest((prevInterest) => [...prevInterest, interestName]);
      updateUserInfo({userInterests: siInterest});
  }


  return (
    <>

    <div className='interest-container'>
      {
        Interests.intereses.map((interest,index)=>(
          <InterestCard key={index} name={interest.nombre} handleInterest={handleInterest}/>
        ))
      }
    </div>

    </>
  )
}

export default Interest