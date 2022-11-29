import { Suspense, lazy } from 'react'

import { AppBar, Box, Button, IconButton, Toolbar, Typography } from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'

import styles from './LandingPage.module.css'
import { RegularContainer, WideContainer } from '../../components/ResponsiveContainers'
import classNames from 'classnames'

const Sidebar = lazy(() => import('../../modules/left-sidebar/Sidebar'))
const RSidebar = lazy(() => import('../../modules/right-sidebar/RSidebar'))

const LandingPage = () => {
  return (
    <div>
      {/* TODO: Create navBar component*/}
      <nav className={styles.navBar}>
        <div className={styles.headerWrapper}>
          <ul>
            {/* <Link href="/sh/dashboard"> */}
            <a className={styles.toolbarButtons}>HINGACU</a>
            {/* </Link> */}
          </ul>

          <ul>
            {/* <Link href="/sh/dashboard"> */}
            <a className={styles.toolbarButtons}>About the Project</a>
            {/* </Link> */}
            {/* <Link href="/sh/dashboard"> */}
            <a className={styles.toolbarButtons}>Project Partners</a>
            {/* </Link> */}
            {/* <Link href="/sh/dashboard"> */}
            <a className={styles.toolbarButtons}>Contact Us</a>
            {/* </Link> */}
          </ul>
        </div>
      </nav>
      <p className={styles.landing}>Landing Page</p>
      <div className={styles.searchBox}>
        <p>HINGACU logo</p>
        <p>Search an area or location to view available mangrove, seagrass, reef, fish and coastline data.</p>
      </div>
    </div>
  )
}

export default LandingPage
