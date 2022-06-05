import React, { useState, useEffect } from "react";
import axios from "axios";

export const AllBeers = () => {

    const [allBeerList, setAllBeerList] = useState([]);
    const [loading, setLoading] = useState(false);

    React.useEffect(() => {
    // var axios = require('axios');

        fetch('/all_beers')
            .then(res => res.json())
            .then(data => setAllBeerList(data.data))
            .catch(err => console.error(err))
        
    }, []);
        
    console.log(Object.entries(allBeerList))

    if (loading) {
        return <p>Data is loading...</p>
    }

    // const beerArray = allBeerList.map(((data) => {
    //     return beerDetails
    // }))
    
    return(
            <div className="beerlist">
                <p>BEER LIST</p>
               
                   <h3>BEER</h3>
                    {allBeerList.map((beer, index) => {
                        return(
                            <div>
                                <ul>
                                <li key={index}>{beer.id}, {beer.name}</li>
                               
                                </ul>
                            </div>
                        )
                        
                    })
                  
                    }
            
            </div>
            
            )
            
        
    };

    

