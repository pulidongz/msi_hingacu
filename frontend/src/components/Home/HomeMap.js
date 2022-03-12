import React, { useState, useRef, useEffect } from 'react'
import Grid from '@mui/material/Grid';
import { createTheme } from '@mui/material/styles';
import L from "leaflet";
import { MapContainer, TileLayer, LayerGroup, WMSTileLayer, LayersControl, useMapEvents, Marker, GeoJSON, useMap, Polyline } from 'react-leaflet'
import CustomWMSLayer from '../../utilities/Leaflet/CustomWMSLayer';
import MapOptionsLayers from './MapOptionsLayers';
import axios from 'axios';
import { render } from '@testing-library/react';
import geojson from './geojson.json';

const { Overlay } = LayersControl;



// import 'react-pro-sidebar/dist/css/styles.css';

const theme = createTheme();

export default function HomeMap () {
	// const map = useMap()
	const karagatanURL = 'http://167.86.124.21:8080/geoserver/karagatan/wms';
	const philcomarsURL = 'http://202.90.159.74:8080/geoserver/philcomars/wms'

	const [data, setData] = React.useState(null);
	const innerBounds = [
		[12.599512, 121.984222],
		[11.630715737981498, 131.04492187500003],
	  ]

	useEffect(() => {
    const getData = async () => {
      const response = await axios.get(
        "http://202.90.159.74:8080/geoserver/philcomars/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=philcomars%3A20180125_reg_boundary&maxFeatures=50&outputFormat=application%2Fjson"
      );
      setData(response.data);
    };
    getData();
  }, []);

	const [position, setPosition] = useState(null)
	const icon = L.icon({
		iconSize: [25, 41],
		iconAnchor: [10, 41],
		popupAnchor: [2, -40],
		iconUrl: "https://unpkg.com/leaflet@1.6/dist/images/marker-icon.png",
		shadowUrl: "https://unpkg.com/leaflet@1.6/dist/images/marker-shadow.png"
	  });

	function ChangeWmsLayer() {
		const [wmsLayer, setWmsLayer] = useState(null);
		const map = useMapEvents({
			click(e) {
				console.log(e.latlng)
			  },
			overlayadd: (e) => {
				console.log("MAP", e.name);
				switch (e.name) {
					case "National Integrated Protected Areas System":
						setWmsLayer(
							<CustomWMSLayer
							layers={['karagatan:Protected Areas']}
							version= '1.1.0'
							crossOrigin='anonymous'
							options={{
								"format": "text/html",
								"transparent": "true",
								"attribution": '<a href="https://eogdata.mines.edu/vbd/">Earth Observation Group, Payne Institute for Public Policy</a>',
								"info_format": "text/html"
							}}
							url={karagatanURL}
							/>	
						);
						break;
					case "Kalayaan Island Group":
						console.log("Kalayaan Island Group");
						break;
					case "Philippine Extended Continental Shelf":
						console.log("Philippine Extended Continental Shelf");
						break;
					case "Fisheries Management Areas":
						console.log("Fisheries Management Areas");
						break;
					case "Philippine Territorial/Internal Waters":
						console.log("Philippine Territorial/Internal Waters");
						break;
					case "Municipal waters-archipelagic principle":
						console.log("Municipal waters-archipelagic principle");
						break;
					case "Municipal waters-mainland principle(hypothetical)":
						console.log("Municipal waters-mainland principle(hypothetical)");
						break;
					case "Regional Boundaries (Philcomars)":
						setWmsLayer(
							<CustomWMSLayer
								layers= {['philcomars:20180125_reg_boundary']}
								version= '1.1.0'
								crossOrigin= 'null'
								options={{
									"format": "text/html",
									"transparent": "true",
									"attribution": '<a href="https://eogdata.mines.edu/vbd/">Earth Observation Group, Payne Institute for Public Policy</a>',
									"info_format": "text/html"
								}}
								url={philcomarsURL}
							/>
						);
						break;
					case "Provincial Boundaries (Philcomars":
						console.log("Provincial Boundaries (Philcomars");
						setWmsLayer(
							<CustomWMSLayer
								layers= {['philcomars:20180125_prov_boundary']}
								version= '1.1.0'
								crossOrigin= 'null'
								options={{
									"format": "text/html",
									"transparent": "true",
									"attribution": '<a href="https://eogdata.mines.edu/vbd/">Earth Observation Group, Payne Institute for Public Policy</a>',
									"info_format": "text/html"
								}}
								url={philcomarsURL}
							/>
						);
						break;
					case "Municipal Boundaries (Philcomars)":
						console.log("Municipal Boundaries (Philcomars)");
						break;
					default:
						return;
				}
			},
			overlayremove: () => {
				setWmsLayer(null);
			},
		});
		return (wmsLayer);
	}

	console.log(data);
	return(
		<MapContainer className="leaflet_home_map" center={[12.599512, 121.984222]} zoom={6} scrollWheelZoom={true} style={{ height: "100vh"}}>
						{/* <MapOptionsLayers /> */}

				<LayersControl position="topright" collapsed={true}>
					<LayersControl.BaseLayer name="NAMRIA">
						<TileLayer
							attribution='© <a href="https:/www.geoportal.gov.ph">Geoportal Philippines</a>'
							url='http://basemapserver.geoportal.gov.ph/tiles/v2/PGP/{z}/{x}/{y}.png'
						/>
					</LayersControl.BaseLayer>
					<LayersControl.BaseLayer checked name="Google Maps">
						<TileLayer
							attribution='© Google <a href="https://developers.google.com/maps/terms">Terms of Use</a>'
							url='http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}&s=Ga'
						/>
					</LayersControl.BaseLayer>
					<LayersControl.BaseLayer name="ESRI World Imagery">
						<TileLayer
							attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
							url='http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
						/>
					</LayersControl.BaseLayer>
					<LayersControl.BaseLayer name="ESRI World Street Map">
						<TileLayer
							attribution='Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
							url='http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}'
						/>
					</LayersControl.BaseLayer>
					
					<LayersControl.Overlay checked name="National Integrated Protected Areas System">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'karagatan:Protected Areas'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay checked name="Kalayaan Island Group">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'karagatan:kalayaanisgroup'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay checked name="Philippine Extended Continental Shelf">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'PhilECS'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay checked name="Mangrove">
						<GeoJSON
							key='1'
							attribution="Mangrove (BlueCARES)"
							data={data}
							pathOptions={{ color: 'red' }}
						/>
					</LayersControl.Overlay>
					{/* <LayersControl.Overlay checked name="Test">
						<Polyline positions={innerBounds} />
					</LayersControl.Overlay> */}
					{/* <LayersControl.Overlay name="Fisheries Management Areas">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'karagatan:fma'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Philippine Territorial/Internal Waters">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'karagatan:territorialwaters'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Municipal waters-archipelagic principle">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'karagatan:municipal_waters'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Municipal waters-mainland principle(hypothetical)">
						<WMSTileLayer
							url={karagatanURL}
							layers= 'karagatan:munwaters_mainland'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
				
					<LayersControl.Overlay name="Regional Boundaries (Philcomars)">
						<WMSTileLayer
							url={philcomarsURL}
							layers= 'philcomars:20180125_reg_boundary'
							version= '1.1.0'
							transparent= {true}
							format= 'image/png'
							// crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Provincial Boundaries (Philcomars)">
						<WMSTileLayer
							url={philcomarsURL}
							layers= 'philcomars:20180125_prov_boundary'
							version= '1.1.0'
							transparent= {true}
							format= 'image/png'
							// crossOrigin='anonymous'
						/>
					</LayersControl.Overlay> */}
					<LayersControl.Overlay name="Municipal Boundaries (Philcomars)">
						<WMSTileLayer
							url={philcomarsURL}
							layers= 'philcomars:20180122_municity_boundary'
							version= '1.1.0'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
				</LayersControl>

				{/* WMS declarations to enable WMS layer popups */}
				
				<ChangeWmsLayer />
			</MapContainer>
	);
}