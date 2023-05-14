import { Link } from 'react-router-dom'
import MapIcon from '@mui/icons-material/Map'
import classNames from 'classnames'

import { AppBar, Box, Button, IconButton, TextField, Toolbar, Typography } from '@mui/material'
import { RegularContainer, WideContainer } from '../../components/layouts/ResponsiveContainers'
import AddressAutocomplete from '../../components/AddressAutocomplete'
import NavBar from '../../components/layouts/NavBar'

import styles from './LandingPage.module.css'

const LandingPage = () => {
  return (
    <div>
      <NavBar />
      <div className={styles.searchBox}>
        <img src="/landing/hingacu_logo.svg" alt="Hingacu"></img>
        <p className={styles.subText}>
          Search an area or location to view available mangrove, seagrass, reef, fish and coastline data.
        </p>
        <AddressAutocomplete />
        <Link to={'/map'}>
          <Button sx={{ marginTop: '16px', backgroundColor: '#319795' }} variant="contained" startIcon={<MapIcon />}>
            Map View
          </Button>
        </Link>
      </div>
    </div>
  )
}

export default LandingPage
