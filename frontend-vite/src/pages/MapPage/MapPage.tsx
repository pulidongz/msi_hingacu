import { Suspense, lazy } from 'react'

import styles from './Home.module.css'
import HomeMap from '../../modules/map/HomeMap'

const Sidebar = lazy(() => import('../../modules/left-sidebar/Sidebar'))
const RSidebar = lazy(() => import('../../modules/right-sidebar/RSidebar'))

const MapPage = () => {
  return (
    <>
      <Sidebar />
      {/* <RSidebar /> */}
    </>
  )
}

export default MapPage
