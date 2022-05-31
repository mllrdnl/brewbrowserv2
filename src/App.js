import logo from './logo.svg';
import './App.css';
import beerfridgelogo from './BeerFridgeGraphic.png';

import { AllBeers } from './frontend/components/AllBeers';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={beerfridgelogo} className="App-logo" alt="logo" /> */}
        </header>
        <body>
        <div className="bodcontainer">
          <div className="bb_logo"></div>

          <div className="beerfridge">
          
            <div className="beercans">
              <div className="blankcan_four"></div>
              <div className="blankcan_one"></div>
              <div className="blankcan_two"></div>
              <div className="blankcan_three"></div>
            
              <div className="ipa"></div>
              <div className="paleale"></div> 
              <div className="lager"></div>
            </div>
          </div>

        <div className="coming_soon">
          <div className="cstextbox">
            <h3>Coming Soon</h3>
          </div>
        </div>

        {/* <h3>All Beers</h3> */}
        
        
      

      {/* <div className="allbeerslist">
      <AllBeers/>
      </div> */}
        </div>
        </body>
    </div>
  );
}

export default App;
