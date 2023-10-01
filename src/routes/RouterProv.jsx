import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Landing from '../views/Landing';
import Login from '../views/Login';
import ErrorPage from '../views/Error-Page';
import Signup from '../views/Signup';
import ThankYou from '../views/ThankYou';
import Home from '../views/Home';

function RouterProv(){
    
    const routes = createBrowserRouter([
        { path:"/", Component:Landing, errorElement: <ErrorPage/>},
        { path: "/home", Component: Home },
        { path: "/login", Component: Login },
        { path: "/signup", Component: Signup },
        { path: "/thankyou", Component: ThankYou },
    ]);
    
    return(
       <RouterProvider router={routes}></RouterProvider>
    )
}


export default RouterProv