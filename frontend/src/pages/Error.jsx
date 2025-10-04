import useRouterError from "react-router-dom";
import NavBar from "../components/NavBar";

function ErrorPage() {

    const error = useRouterError();
    const status = error.status || 500;
    const message = error.statusText || error.message || "Something went wrong.";

    console.error(error);

return (
<>
<header>
    <NavBar />
</header>
<main>
    <h1>{status}</h1>
    <p>{message}</p>  
</main>
</>
)}

export default ErrorPage
