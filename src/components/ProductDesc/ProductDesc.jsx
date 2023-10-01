import AOS from 'aos'
import 'aos/dist/aos.css'
import { useEffect } from 'react'

const PdescImage = 'PdescImage.png'
const PdescImagePath = `/static/${PdescImage}`

function ProductDesc(){
    useEffect(()=>{
        AOS.init();
    },[])
    return(
        <>
            <div className="productdesc_container">
                <div className="wrapper productdesc_container_content">
                    <div className="product-description">
                        <h2 data-aos='zoom-in'>
                            Leave 
                            <br />
                            <b>Everything</b>
                            <br />
                            In our hands            
                        </h2>
                        <div className="product-description-text">
                            <p data-aos='zoom-in'>
                                Based on your preferences, we recommend the best properties from sites such as Metro Cuadrado, Booking and Tripadvidsor.
                            </p>
                            <h4 data-aos='zoom-in'>
                                +1000
                                <br />
                                Houses
                            </h4>
                        </div>
                    </div>
                    <div className="product_image" data-aos='zoom-in'>
                        <img src={PdescImagePath} alt="product_image"/>
                    </div>
                </div>
            
            </div>
        </>
    )
}

export default ProductDesc