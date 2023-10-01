import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect } from 'react'
import { Link } from "react-router-dom";

function Hero(){

    useEffect(()=>{
        AOS.init({duration:1000});
    },[])

    return(
        <>
        <div className="hero_container">
            <div className="wrapper hero_container_content-container">
                <div className="hero_container_content-container_cont">
                    <h2 className="hero_text" data-aos='fade'>
                        Find the property of your dreams
                    </h2>
                        <Link to={`/login`}>
                            <button className="start-btn" data-aos='fade-up'>
                                Start Here
                            </button>    
                        </Link> 
                </div>
            </div>
        </div>
        </>
    )
}

export default Hero