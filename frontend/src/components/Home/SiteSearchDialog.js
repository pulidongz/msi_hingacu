import React, { useState, useRef, useEffect } from 'react'
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Grid from '@mui/material/Grid';
import {regions, provinces, cities, barangays} from 'select-philippines-address';

export default function SiteSearch() {
  const regionOptions = regions.map((option) => {
    const firstLetter = option.region_name[0].toUpperCase();
    return {
      firstLetter: /[0-9]/.test(firstLetter) ? '0-9' : firstLetter,
      ...option,
    };
  });

	const provinceOptions = regions.map((option) => {
    const firstLetter = option.province_name[0].toUpperCase();
    return {
      firstLetter: /[0-9]/.test(firstLetter) ? '0-9' : firstLetter,
      ...option,
    };
  });

	const cityOptions = cities.map((option) => {
    const firstLetter = option.city_name[0].toUpperCase();
    return {
      firstLetter: /[0-9]/.test(firstLetter) ? '0-9' : firstLetter,
      ...option,
    };
  });

	const barangaysOptions = barangays.map((option) => {
    const firstLetter = option.brgy_name[0].toUpperCase();
    return {
      firstLetter: /[0-9]/.test(firstLetter) ? '0-9' : firstLetter,
      ...option,
    };
  });

  const [regionData, setRegion] = useState([]);
	const [provinceData, setProvince] = useState([]);
	const [cityData, setCity] = useState([]);
	const [barangayData, setBarangay] = useState([]);

	const [regionAddr, setRegionAddr] = useState("");
	const [provinceAddr, setProvinceAddr] = useState("");
	const [cityAddr, setCityAddr] = useState("");
	const [barangayAddr, setBarangayAddr] = useState("");

	const region = () => {
		regions().then(response => {
				setRegion(response);
		});
	}
	const province = (e) => {
			setRegionAddr(e.target.selectedOptions[0].text);
			provinces(e.target.value).then(response => {
					setProvince(response);
					setCity([]);
					setBarangay([]);
			});
	}
	const city = (e) => {
			setProvinceAddr(e.target.selectedOptions[0].text);
			cities(e.target.value).then(response => {
					setCity(response);
			});
	}
	const barangay = (e) => {
			setCityAddr(e.target.selectedOptions[0].text);
			barangays(e.target.value).then(response => {
					setBarangay(response);
			});
	}
	const brgy = (e) => {
			setBarangayAddr(e.target.selectedOptions[0].text);
	}
	useEffect(() => {
			region()
	}, [])


  return (
    <React.Fragment>
			<Grid container spacing={1} direction="column" justifyContent="center" alignItems="center">
				<Grid item xs={12}>
					<Autocomplete
						id="auto-region"
						size="small"
						options={regionOptions.sort((a, b) => -b.firstLetter.localeCompare(a.firstLetter))}
						groupBy={(regionOptions) => regionOptions.region_name}
						getOptionLabel={(regionOptions) => regionOptions.region_name}
						sx={{ width: 300 }}
						renderInput={(params) => <TextField {...params} label="Region" />}
					/>
				</Grid>
				{/* <Grid item xs={12}>
					<Autocomplete
						id="auto-province"
						size="small"
						options={options.sort((a, b) => -b.firstLetter.localeCompare(a.firstLetter))}
						groupBy={(option) => option.firstLetter}
						getOptionLabel={(option) => option.title}
						sx={{ width: 300 }}
						renderInput={(params) => <TextField {...params} label="Province" />}
					/>
				</Grid>
				<Grid item xs={12}>
					<Autocomplete
						id="auto-city"
						size="small"
						options={options.sort((a, b) => -b.firstLetter.localeCompare(a.firstLetter))}
						groupBy={(option) => option.firstLetter}
						getOptionLabel={(option) => option.title}
						sx={{ width: 300 }}
						renderInput={(params) => <TextField {...params} label="City/Municipality" />}
					/>
				</Grid>
				<Grid item xs={12}>
					<Autocomplete
						id="auto-brgy"
						size="small"
						options={options.sort((a, b) => -b.firstLetter.localeCompare(a.firstLetter))}
						groupBy={(option) => option.firstLetter}
						getOptionLabel={(option) => option.title}
						sx={{ width: 300 }}
						renderInput={(params) => <TextField {...params} label="Barangay" />}
					/>
				</Grid> */}
			</Grid>
    </React.Fragment>
  );
}

