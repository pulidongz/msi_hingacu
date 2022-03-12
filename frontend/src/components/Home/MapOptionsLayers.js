import React, { useState, useRef, useEffect } from 'react'
import { GeoJSON } from 'react-leaflet';
import axios from 'axios';


export default function MapOptionsLayers(props){
	const [data, setData] = React.useState(null);

	useEffect(() => {
    const getData = async () => {
      const response = await axios.get(
        "http://202.90.159.74:8080/geoserver/philcomars/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=philcomars%3A20180125_reg_boundary&maxFeatures=50&outputFormat=application%2Fjson"
      );
      setData(response.data);
    };
    
  }, []);

	return(
		<GeoJSON
			attribution="Mangrove (BlueCARES)"
			data={data}
			style={() => ({
				color: "green",
				weight: 3,
				opacity: 0.5
			})}
		/>
	);
}