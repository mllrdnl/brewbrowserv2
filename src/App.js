import logo from './logo.svg';
import './App.css';
import beerfridgelogo from './BeerFridgeGraphic.png';

import { AllBeers } from './frontend/components/AllBeers';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={beerfridgelogo} className="App-logo" alt="logo" /> */}

        <div className="beerfridge">
          
          <div className="beercans">
            <div className="blankcan_one"></div>
            <div className="ipa"></div>
            <div className="blankcan_two"></div>
          <div className="paleale"></div> 
          <div className="lager"></div>
          </div>
          
        </div>

        <h3>All Beers</h3>
        
        
      </header>
      <div className="allbeerslist">
      <AllBeers/>
      </div>
        

    </div>
  );
}

export default App;
