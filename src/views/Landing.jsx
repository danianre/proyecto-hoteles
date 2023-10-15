import ProductDesc from '../components/ProductDesc/ProductDesc'
import Header from '../components/Header/Header'
import Hero from '../components/Hero/Hero'
import WhoSection from '../components/WhoSection/WhoSection'
import MayFindSect from '../components/MayFind/MayFindSect'
import Footer from '../components/Footer/Footer'
import JoinUs from '../components/JoinUs/JoinUs'


function Landing(){
    return(
        <>
            <Header/>
            <Hero/>
            <WhoSection/>
            <ProductDesc/>
            <MayFindSect/>
            <JoinUs/>
            <Footer/>
        </>
    )
}
export default Landing