import React, { useState } from 'react'

function InterestCard({name,handleInterest}) {

    const[clicked, setClicked] = useState(false);

    const handleClick = () =>{
        setClicked(!clicked)
        handleInterest(name)
    };

  return (
    <div className={`interest-card ${clicked ? 'active' : ''}`} onClick={handleClick}>
        {clicked ? <span>&#10003; {name}</span> : <p>{name}</p>}
    </div>
  )
}

export default InterestCard