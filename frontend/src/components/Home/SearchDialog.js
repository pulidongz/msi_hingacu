import React, { useState, useRef, useEffect } from 'react'
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Grid from '@mui/material/Grid';
import {regions, provinces, cities, barangays} from 'select-philippines-address';


export default function SearchDialog() {
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
			setRegionAddr(e.target.value);
			provinces(e.target.value).then(response => {
					setProvince(response);
					setCity([]);
					setBarangay([]);
			});
	}
	const city = (e) => {
			setProvinceAddr(e.target.value);
			cities(e.target.value).then(response => {
					setCity(response);
			});
	}
	const barangay = (e) => {
			setCityAddr(e.target.value);
			barangays(e.target.value).then(response => {
					setBarangay(response);
			});
	}
	const brgy = (e) => {
			setBarangayAddr(e.target.value);
	}
	useEffect(() => {
			region()
	}, [])

  console.log(regionAddr, provinceAddr, cityAddr, barangayAddr);

  return (
    <Box sx={{ minWidth: 300 }}>
    <Grid container spacing={2} direction="column" justifyContent="center" alignItems="stretch">
      <Grid item xs={12}>
        <FormControl fullWidth variant="filled" size="small">
          <InputLabel id="demo-simple-select-label">Region</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="select-region"
            size="small"
            value={regionAddr}
            label="Region"
            onChange={province}
          >
            <MenuItem disabled>Select Region</MenuItem>
            {
              regionData && regionData.length > 0 && regionData.map((item) => 
              <MenuItem
                key={item.region_code} value={item.region_code}>{item.region_name}
              </MenuItem>)
            }
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={12}>
        <FormControl fullWidth variant="filled" >
          <InputLabel id="demo-simple-select-label">Province</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="select-province"
            size="small"
            value={provinceAddr}
            label="Province"
            onChange={city}
          >
            <MenuItem disabled>Select Province</MenuItem>
            {
              provinceData && provinceData.length > 0 && provinceData.map((item) => <MenuItem
                key={item.province_code} value={item.province_code}>{item.province_name}
              </MenuItem>)
            }
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={12}>
        <FormControl fullWidth variant="filled" >
          <InputLabel id="demo-simple-select-label">City/Municipality</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="select-city"
            size="small"
            value={cityAddr}
            label="City"
            onChange={barangay}
          >
            <MenuItem disabled>Select City/Municipality</MenuItem>
            {
              cityData && cityData.length > 0 && cityData.map((item) => 
              <MenuItem
                key={item.city_code} value={item.city_code}>{item.city_name}
              </MenuItem>)
            }
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={12}>
        <FormControl fullWidth variant="filled" >
          <InputLabel id="demo-simple-select-label">Barangay</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="select-barangay"
            size="small"
            value={barangayAddr}
            label="Barangay"
            onChange={brgy}
          >
            <MenuItem disabled >Select Barangay</MenuItem>
            {
              barangayData && barangayData.length > 0 && barangayData.map((item) =>
              <MenuItem
                key={item.brgy_code} value={item.brgy_code}>{item.brgy_name}
              </MenuItem>)
            }
          </Select>
        </FormControl>
      </Grid>
    </Grid>
    </Box>
  );
}