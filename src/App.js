import logo from './logo.svg';
import './App.css';
import beerfridgelogo from './BeerFridgeGraphic.png';

import { AllBeers } from './frontend/components/AllBeers';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={beerfridgelogo} className="App-logo" alt="logo" />

        <h3>All Beers</h3>
        <AllBeers/>
        

        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
