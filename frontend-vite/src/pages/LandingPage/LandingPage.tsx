import { Suspense, lazy } from 'react'

import { AppBar, Box, Button, IconButton, Toolbar, Typography } from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'

import styles from './LandingPage.module.css'

const Sidebar = lazy(() => import('../../modules/left-sidebar/Sidebar'))
const RSidebar = lazy(() => import('../../modules/right-sidebar/RSidebar'))

const LandingPage = () => {
  return (
    <div className={styles.landingPageContainer}>
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <IconButton size="large" edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              About the Project
            </Typography>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Project Partners
            </Typography>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Contact Us
            </Typography>

            {/* <Button color="inherit">Login</Button> */}
          </Toolbar>
        </AppBar>
      </Box>

      <p>Landing Page</p>
    </div>
  )
}

export default LandingPage
