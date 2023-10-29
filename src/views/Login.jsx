import { Link } from "react-router-dom"

const logogid = 'logogid.png'
const logogidPath = `./static/${logogid}`

function Login(){
    const handleSubmit = async (e) => {
        e.preventDefault();
        const email = e.target.email.value;
        const password = e.target.password.value;
    
        const data = { email, password };
    
        try {
          const response = await fetch('/login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
          });
    
          if (response.ok) {
            // El inicio de sesión fue exitoso, puedes redirigir al usuario o realizar alguna acción adicional
            // Por ejemplo, redirigir a la página principal
            window.location.href = '/home';
          } else {
            // El inicio de sesión falló, puedes mostrar un mensaje de error al usuario
            console.error('Error al iniciar sesión');
          }
        } catch (error) {
          console.error('Error en la solicitud:', error);
        }
      };
    return(
        <>
        <div className="login-container">
            <div className="grid-el login-image"></div>
            <div className="grid-el login-content">
                <div className="login-content-logo">
                    <img src={logogidPath} alt="logo" />
                    <h1>Welcome!</h1>
                </div>
                <div>
                    <form className="login-content-form" onSubmit={handleSubmit}>
                        <label htmlFor="email">Email</label>
                        <input type="email" name="email" id="email-login" placeholder="Escribe tu email"/>
                        <label htmlFor="passw">Password</label>
                        <input type="passw" name="password" id="passw-login" placeholder="Escribe tu  password"/>
                        <input type="submit" value="Log In"  id="submit-login"/>
                    </form>
                </div>
                <p style={{textAlign:"center"}}>New over here? <Link to={'/signup/'}><a href="#">Create an account!</a></Link></p>
            </div>
        </div>
        </>
    )
}
export default Login