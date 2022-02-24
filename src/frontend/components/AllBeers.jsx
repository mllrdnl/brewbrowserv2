import React, { useState } from "react";
import axios from "axios";

export const AllBeers = () => {
    
    const [allBeerList, setAllBeerList] = useState([]);

    // var axios = require('axios');

    function getAllBeerList() {
        axios({
            method: "GET",
            url: "https://api.catalog.beer/beer",
            headers: {
                "accept": "application/json",
                "Authorization": "Basic NTFjODNhNDctODEwOS00YTEyLTlkMjctNDM1MjA1YTEzZDgzOg==",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': "get,has,keys,set,values,Authorization"
            }
        })
        .then((response) => {
            const res = JSON.stringify(response.data)

            setAllBeerList(({
                id: res.id,
                name: res.name
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
                    {allBeerList.map((beer, index) => {
                        return(
                            <li key={index}>{beer.id}</li>
                        )
                    })}
                </ul>
            </div>
        )
    };
    

