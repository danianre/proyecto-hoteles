import { Link } from "react-router-dom"

const logogid = 'logogid.png'
const logogidPath = `./static/${logogid}`

function Login(){
    return(
        <>
        <div className="login-container">
            <div className="grid-el login-image">
            </div>
            <div className="grid-el login-content">
                <div className="login-content-logo">
                    <img src={logogidPath} alt="logo" />
                    <h1>Welcome!</h1>
                </div>
                <div className="login-content-form">
                    <label htmlFor="email">Email</label>
                    <input type="email" name="email" id="email-login" placeholder="Type your email"/>
                    <label htmlFor="passw">Password</label>
                    <input type="password" name="passw" id="passw-login" placeholder="Type your password"/>
                    <input type="submit" value="Log In"  id="submit-login"/>
                </div>
                <p style={{textAlign:"center"}}>New over here? <Link to={'/signup'}><a href="#">Create an account!</a></Link></p>
            </div>
        </div>
        </>
    )
}
export default Login