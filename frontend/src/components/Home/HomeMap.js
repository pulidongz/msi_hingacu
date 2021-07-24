import React, { useState } from 'react'
import Grid from '@material-ui/core/Grid';
import createMuiTheme from "@material-ui/core/styles/createMuiTheme";
import { MapContainer, TileLayer, WMSTileLayer, LayersControl } from 'react-leaflet'
import CustomWMSLayer from '../../utilities/Leaflet/CustomWMSLayer';
import 'react-pro-sidebar/dist/css/styles.css';

const theme = createMuiTheme();

export default function HomeMap () {
	const karagatanURL = 'http://167.86.124.21:8080/geoserver/karagatan/wms';

	return(
		<MapContainer className="leaflet_home_map" center={[12.599512, 121.984222]} zoom={6} scrollWheelZoom={true} style={{ height: "100vh"}}>
				<LayersControl position="topright" collapsed={false}>
					<LayersControl.BaseLayer checked name="NAMRIA Basemap">
						<TileLayer
							attribution='© <a href="https:/www.geoportal.gov.ph">Geoportal Philippines</a>'
							url='http://basemapserver.geoportal.gov.ph/tiles/v2/PGP/{z}/{x}/{y}.png'
						/>
					</LayersControl.BaseLayer>
					<LayersControl.BaseLayer name="Google Map">
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
					<LayersControl.Overlay name="Fisheries Management Areas">
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
				</LayersControl>

				{/* WMS declarations to enable WMS layer popups */}
				<CustomWMSLayer
					layers={['karagatan:Protected Areas']}
					version= '2.15.1'
					crossOrigin='anonymous'
					options={{
						"format": "text/html",
						"transparent": "true",
						"attribution": '<a href="https://eogdata.mines.edu/vbd/">Earth Observation Group, Payne Institute for Public Policy</a>',
						"info_format": "text/html"
					}}
					url={karagatanURL}
				/>
			</MapContainer>
	);
}