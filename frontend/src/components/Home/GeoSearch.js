import React, { useState, useRef, useEffect } from 'react'
import { TextField, Autocomplete, CircularProgress, Box, Grid } from '@mui/material';
import SearchRoundedIcon from '@mui/icons-material/SearchRounded';
import { OpenStreetMapProvider } from 'leaflet-geosearch';

const provider = new OpenStreetMapProvider({
  params: {
    countrycodes: 'ph',
    addressdetails: 1,
  },
});

const results = async (query) => {
	const results = await provider.search({ query:query });
	return results.map(result => ({
		lon: result.x,
		lat: result.y,
		label: result.label,
	}));
}

export default function GeoSearch(){
  const [location, setLocation] = useState("");
	const [open, setOpen] = useState(false);
	const [options, setOptions] = useState([]);
	const loading = open && options.length === 0;

	useEffect(() => {
		let active = true;

    if (!loading) {
      return undefined;
    }

    (async () => {
      const res = await results(location);
			console.log(res);

      if (active) {
        setOptions(res);
      }
    })();

    return () => {
      active = false;
    };
	}, [loading]);

	const handleChangeOptions = async(e, value) => {
		const results = await provider.search({ query: value });
		setOptions(results);
	}

	const handleChangeLocation = (e, value) => {
		setLocation(value);
		console.log("Location: ", value);
	}

	return(
		<Box sx={{ minWidth: 300 }}>
    <Grid container spacing={2} direction="column" justifyContent="center" alignItems="stretch">
			<Grid item xs={12}>
			<Autocomplete
				freeSolo
				autoSelect
				autoHighlight
				// clearOnBlur
				clearOnEscape
				disableClearable
				// disableCloseOnSelect
				size="small"
				id="asynchronous-demo"
				sx={{ width: 300 }}
				value={location}
				open={open}
				onOpen={() => { setOpen(true); }}
				onClose={() => { setOpen(false); }}
				loading={loading}
				onChange={ handleChangeLocation }
				onInputChange={(e, value) => {
					handleChangeOptions(e, value);
					if(!value){
						setOpen(false);
					}
				}}
				options={options}
				getOptionLabel={ (option) => option.label ? option.label : "" }
				renderInput={(params) => (
					<TextField
						{...params}
						label="Search Site"
						variant="outlined"
						InputProps={{
							...params.InputProps,
							type: 'search',
							endAdornment: (
								<React.Fragment>
									{<SearchRoundedIcon color="primary" size={20} />}
									{params.InputProps.endAdornment}
								</React.Fragment>
							),
						}}
					/>
				)}
			/>

			</Grid>
		</Grid>
		</Box>
	);
}