import React, { useState } from "react";
import axios from "axios";

export const AllBeers = () => {
    
    const [allBeerList, setAllBeerList] = useState([]);

    // var axios = require('axios');

    function getAllBeerList() {
        axios({
            method: "GET",
            url: "/all_beers",
           
        })
        .then((response) => {
            // const res = res.json()
            // const data = setAllBeerList(data.response.text)
            const res = JSON.stringify(response.data)

            setAllBeerList(({
                object: res.object,
                names: res.data
            }))
        }).catch((error) => {
            if (error.response) {
              console.log(error.response)
              console.log(error.response.status)
              console.log(error.response.headers)
              }
          })}

        return(
            <div className="beerlist">
                <p>BEER LIST</p>
                <button onClick={getAllBeerList}>Get it</button>
                    <ul>
                    {allBeerList.map((beerData, index) => {
                        return(
                            <div>
                            <h3>{beerData.object}</h3>
                            { beerData.data.map((beer, i) => {
                                return(
                                    <li key={i}>{beer.id}, {beer.name}</li>
                                )
                            })}
                            
                            {/* <li key={index}>{beer.id}</li> */}
                            
                            </div>
                        )
                    })}
                    </ul>
                
            </div>
        )
    };
    

