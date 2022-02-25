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
        // axios({
        //     method: "GET",
        //     url: "/all_beers",
        
        // })
        // .then((response) => {
        //     const res = response.data

        //     const data = res.data    
            
        //     setAllBeerList(data.data)


        // }).catch((error) => {
        //     if (error.response) {
        //     console.log(error.response)
        //     console.log(error.response.status)
        //     console.log(error.response.headers)
        //     }
        // })}
    console.log(Object.entries(allBeerList))

    if (loading) {
        return <p>Data is loading...</p>
    }
    
    return(
            <div className="beerlist">
                <p>BEER LIST</p>
                {/* <button onClick={getAllBeerList}>Get it</button> */}
                    <ul>
                    {/* {allBeerList.map(({id, name }) => {
                        
                            <div>
                                <h3>BEER</h3>
                                <li key={id}>{id}, {name}</li>
                            </div>
                        
                    })} */}
                  
                    </ul>
            
            </div>
            
            )
            
        
    };

    

