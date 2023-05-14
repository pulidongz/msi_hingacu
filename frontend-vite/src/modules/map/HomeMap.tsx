import { ReactNode } from 'react'
import { MapContainer, TileLayer } from 'react-leaflet'

import MapFlyToLocation from '../../lib/helpers/MapFlyToLocation'

import 'leaflet/dist/leaflet.css'
import NavBar from '../../components/layouts/NavBar'
import RSidebar from '../right-sidebar/RSidebar'

type HomeMapProps = {
  children?: ReactNode
}

const HomeMap = ({ children }: HomeMapProps) => {
  return (
    <>
      {/* <RSidebar /> */}

      <MapContainer
        center={[12.599512, 121.984222]}
        zoom={6}
        scrollWheelZoom={false}
        style={{ height: '100vh', width: '100%' }}
      >
        <TileLayer
          attribution='© <a href="https:/www.geoportal.gov.ph">Geoportal Philippines</a>'
          url="http://basemapserver.geoportal.gov.ph/tiles/v2/PGP/{z}/{x}/{y}.png"
        />

        {/* TODO: Insert trigger functions i.e. zoom to searched locations, show graphs, tables, etc*/}
        {/* <MapFlyToLocation /> */}

        {/* <div>{children && children}</div> */}

        <RSidebar />
      </MapContainer>
    </>
  )
}

export default HomeMap
