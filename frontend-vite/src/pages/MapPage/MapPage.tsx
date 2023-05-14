import { Suspense, lazy } from 'react'

import styles from './Home.module.css'
import HomeMap from '../../modules/map/HomeMap'
import NavBar from '../../components/layouts/NavBar'

const Sidebar = lazy(() => import('../../modules/left-sidebar/Sidebar'))
const RSidebar = lazy(() => import('../../modules/right-sidebar/RSidebar'))

const MapPage = () => {
  return (
    <>
      {/* TODO: Use useContext to pass MapDataProps (lon, lat, etc. to children components) */}
      <Sidebar />
      {/* <RSidebar /> */}
      {/* <HomeMap> */}
      {/* <Sidebar /> */}
      {/* <RSidebar /> */}
      {/* <NavBar /> */}
      {/* </HomeMap> */}
    </>
  )
}

export default MapPage
