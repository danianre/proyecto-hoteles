import React from 'react'
import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect } from 'react'

function MayFindCard(props) {

  useEffect(()=>{
    AOS.init({duration:1000});
  },[])

  return (
    <div className='mayfindcard-container' data-aos='fade-up'>
        <div className="mayfindcard-img">
          <img src={props.product.imagen} alt="img-card" />
        </div>
        <div className="mayfindcard-desc">
          <p>{props.product.producto}</p>
          <p>{props.product.desc}</p>
          </div>
    </div>
  )
}

export default MayFindCard