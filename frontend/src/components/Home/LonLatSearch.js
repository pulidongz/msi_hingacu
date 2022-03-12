import React, { useState, useRef, useEffect } from 'react'
import { TextField, Autocomplete, CircularProgress, Box, Grid, Button, Typography } from '@mui/material';

export default function LonLatSearch(){
 
    return(
			<React.Fragment>
				
				<Grid container direction="column" justifyContent="center" alignItems="center" spacing={1}>
					<Grid item xs={12}>
					</Grid>
	 				<Grid item xs={12}>
						<Typography variant="caption" gutterBottom>Please input the coordinates:</Typography>
					</Grid>
					<Grid item xs={6}>
						<TextField
							label="Longitude"
							id="longitude"
							placeholder="0.0"
							size="small"
							type="number"
						/>
					</Grid>
					<Grid item xs={6}>
						<TextField
							label="Latitude"
							id="latitude"
							placeholder="0.0"
							size="small"
							type="number"
						/>
					</Grid>
					<Grid item xs={12}>
					</Grid>
					<Grid container direction="row" justifyContent="center" alignItems="center" spacing={1}>
						<Grid item xs={6}>
							<Button variant="text" size="small">Deg-Min-Sec</Button>
						</Grid>
						<Grid item xs={6}>
							<Button variant="contained">Search</Button>
						</Grid>
					</Grid>
				</Grid>
			</React.Fragment>
    );
}