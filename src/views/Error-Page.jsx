import {useRouteError} from "react-router-dom"

function ErrorPage(){
    const error = useRouteError();
    return(
        <div style={{color:"white",display:"flex", justifyContent:"center",textAlign:"center", flexDirection:"column", position:"absolute", top:"50%", left:"50%", transform:"translate(-50%,-50%)"}}>
            <h1 style={{color:"white"}}>
                Ohh no!
            </h1>
            <p><b>An error has ocurred</b></p>
            <p>{error.statusText || error.message}</p>
        </div>
    )
}

export default ErrorPage