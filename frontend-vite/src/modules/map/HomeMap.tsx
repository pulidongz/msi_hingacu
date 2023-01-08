import { MapContainer, TileLayer, useMap } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

const HomeMap = () => {
  return (
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
    </MapContainer>
  )
}

export default HomeMap
