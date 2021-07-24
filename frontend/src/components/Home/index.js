import React, { useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { ThemeProvider }  from "@material-ui/core/styles";
import Grid from '@material-ui/core/Grid';
import Fab from '@material-ui/core/Fab';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import InputAdornment from '@material-ui/core/InputAdornment';
import IconButton from '@material-ui/core/IconButton';
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import Box from '@material-ui/core/Box';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';

import createMuiTheme from "@material-ui/core/styles/createMuiTheme";

import { useHistory } from 'react-router-dom';

import { MapContainer, TileLayer, WMSTileLayer, LayersControl, FeatureGroup, Popup, Circle, Reactangle } from 'react-leaflet'
import CustomWMSLayer from '../../utilities/Leaflet/CustomWMSLayer';
import { LayerGroup } from 'leaflet';

const theme = createMuiTheme();

export default function Home () {
	let history = useHistory();
	const karagatanURL = 'http://167.86.124.21:8080/geoserver/karagatan/wms';

	return(
		<Grid container direction="row"
		justify="center"
		alignItems="center">
			<MapContainer className="leaflet_home_map" center={[12.599512, 121.984222]} zoom={6} scrollWheelZoom={true} style={{ height: "100vh", width: "100vw"}}>

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
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
							layers= 'karagatan:Protected Areas'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay checked name="Kalayaan Island Group">
						<WMSTileLayer
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
							layers= 'karagatan:kalayaanisgroup'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay checked name="Philippine Extended Continental Shelf">
						<WMSTileLayer
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
							layers= 'PhilECS'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Fisheries Management Areas">
						<WMSTileLayer
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
							layers= 'karagatan:fma'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Philippine Territorial/Internal Waters">
						<WMSTileLayer
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
							layers= 'karagatan:territorialwaters'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Municipal waters-archipelagic principle">
						<WMSTileLayer
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
							layers= 'karagatan:municipal_waters'
							version= '2.15.1'
							transparent= {true}
							format= 'image/png'
							crossOrigin='anonymous'
						/>
					</LayersControl.Overlay>
					<LayersControl.Overlay name="Municipal waters-mainland principle(hypothetical)">
						<WMSTileLayer
							url='http://167.86.124.21:8080/geoserver/karagatan/wms'
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
					url="http://167.86.124.21:8080/geoserver/karagatan/wms"
				/>
		</MapContainer>
		</Grid>
		
	);
}