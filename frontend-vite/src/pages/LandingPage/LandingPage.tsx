import { Suspense, lazy } from 'react'
import classNames from 'classnames'

import { AppBar, Box, Button, IconButton, TextField, Toolbar, Typography } from '@mui/material'
import { RegularContainer, WideContainer } from '../../components/layouts/ResponsiveContainers'
import NavBar from '../../components/layouts/NavBar'

import styles from './LandingPage.module.css'

const Sidebar = lazy(() => import('../../modules/left-sidebar/Sidebar'))
const RSidebar = lazy(() => import('../../modules/right-sidebar/RSidebar'))

const LandingPage = () => {
  return (
    <div>
      <NavBar />
      <div className={styles.searchBox}>
        <img src="/landing/hingacu_logo.svg" alt="Hingacu"></img>
        <p className={styles.subText}>
          Search an area or location to view available mangrove, seagrass, reef, fish and coastline data.
        </p>
        <TextField variant="outlined" placeholder="Search Location" sx={{ width: '100%' }}></TextField>
      </div>
      ``
    </div>
  )
}

export default LandingPage
