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

import { MapContainer, TileLayer, LayersControl } from 'react-leaflet'

const theme = createMuiTheme();

export default function Home () {
	let history = useHistory();

	return(
		<Grid container direction="row"
		justify="center"
		alignItems="center">
			<MapContainer className="leaflet_home_map" center={[12.599512, 121.984222]} zoom={6} scrollWheelZoom={false} style={{ height: "100vh" }}>
				<LayersControl position="topright" collapsed={false}>
						<LayersControl.BaseLayer checked name="ESRI World Imagery">
							<TileLayer
								attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
								url="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
							/>
						</LayersControl.BaseLayer>
						<LayersControl.BaseLayer name="ESRI World Street Map">
							<TileLayer
								attribution='Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
								url="http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}"
							/>
						</LayersControl.BaseLayer>
			</LayersControl>
		</MapContainer>
		</Grid>
		
	);
}