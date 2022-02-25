import React, { useState } from "react";
import axios from "axios";

export const AllBeers = () => {

    const [beerListObj, setBeerListObj] = useState({});
    const [allBeerList, setAllBeerList] = useState([]);

    // var axios = require('axios');

    function getAllBeerList() {
        axios({
            method: "GET",
            url: "/all_beers",
           
        })
        .then((response) => {
            const res = response.data

            const data = res.data    
            
            setAllBeerList(data.data)


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
                    {allBeerList.map((beer, index) => {
                        return(
                            <div>
                                <h3>BEER</h3>
                                <li key={index}>{beer.id}, {beer.name}</li>
                            </div>
                        )
                    })}
                  
                    </ul>
            
            </div>
            
            )
            
        
    };

    

