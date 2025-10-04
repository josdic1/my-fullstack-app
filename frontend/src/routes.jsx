import App from './App.jsx'
import ErrorPage from './pages/Error.jsx'

const routes = [
    {
        path: '/',
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                index: true,
                element: <h2>Home Page</h2>
            }
        ]
    }
]

export default routes