import { SetStateAction, useState } from 'react'
import { Marker, Popup, useMap, useMapEvents } from 'react-leaflet'

type MapFlyToLocationProps = {
  latitude?: number
  longitude?: number
}

const MapFlyToLocation = ({ latitude, longitude }: MapFlyToLocationProps) => {
  const [position, setPosition] = useState(null)
  const map = useMap()

  if (latitude && longitude) {
    map.flyTo([latitude, longitude], 12)
  } else {
    map.locate()

    map.on('locationfound', (e: { latlng: SetStateAction<null> }) => {
      setPosition(e.latlng)
      map.flyTo(e.latlng, 12)
    })
  }

  return position === null ? null : (
    <Marker position={position}>
      <Popup>You are here</Popup>
    </Marker>
  )
}

export default MapFlyToLocation
