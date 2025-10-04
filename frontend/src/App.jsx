import { Outlet } from 'react-router-dom';
import NavBar from './components/NavBar';

function App() {
  
  return (
    <>
    <header className="App">
      <NavBar />
    </header>
      <main>
        <Outlet />
      </main>
    </>
  );
}


export default App;