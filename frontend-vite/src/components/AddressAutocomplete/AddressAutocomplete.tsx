import { useState } from 'react'
import classNames from 'classnames'
import GooglePlacesAutocomplete, { geocodeByPlaceId } from 'react-google-places-autocomplete'

import styles from './AddressAutocomplete.module.css'

const GOOGLE_MAPS_API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY

type AddressAutocompleteProps = {
  className?: string
  disabled?: boolean
  placeholder?: string
}

type Address = {
  formattedAddress: string
  latitude: number
  longitude: number
  placeId: string
  locationType: string
}

export type AddressAutocompleteArguments = {
  label: string
  value: Address | null
}

const AddressAutocomplete = ({ className, disabled, placeholder }: AddressAutocompleteProps) => {
  const [addressValue, setAddressValue] = useState<AddressAutocompleteArguments | null>(null)

  const resetAddresses = () => {
    setAddressValue({
      label: '',
      value: null
    })
  }

  return (
    <div className={classNames(styles.container, className)}>
      <GooglePlacesAutocomplete
        apiKey={GOOGLE_MAPS_API_KEY}
        debounce={250}
        autocompletionRequest={{
          componentRestrictions: {
            country: ['ph']
          }
        }}
        selectProps={{
          isClearable: true,
          className: classNames(className, styles.inputContainer),
          value: addressValue,
          onChange: (selected: any) => {
            if (selected!) {
              geocodeByPlaceId(selected.value.place_id)
                .then(results =>
                  setAddressValue({
                    label: results[0].formatted_address,
                    value: {
                      formattedAddress: results[0].formatted_address,
                      latitude: results[0].geometry.location.lat(),
                      longitude: results[0].geometry.location.lng(),
                      placeId: results[0].place_id,
                      locationType: results[0].types[0]
                    }
                  })
                )
                .catch(error => console.error(error))
            } else {
              resetAddresses()
            }
          },
          styles: {
            control: (provided: any) => ({
              ...provided,
              backgroundColor: disabled ? 'var(--colorGray1)' : 'var(--colorWhite)',
              border: 0,
              boxShadow: 'none',
              borderRadius: 2,
              minHeight: '30px'
            }),
            container: (provided: any, { isFocused }: any) => ({
              ...provided,
              width: '100%',
              border: '1px solid var(--colorGray8)',
              borderRadius: '5px'
            }),
            option: (provided: any, { isSelected, isFocused, isDisabled }: any) => ({
              ...provided,
              backgroundColor: isSelected ? '' : isFocused ? 'var(--colorGray1)' : 'white',
              color: 'var(--colorGray8)',
              '&:hover': {
                backgroundColor: 'var(--colorGray1)'
              },
              cursor: isDisabled ? 'not-allowed' : 'pointer'
            }),
            indicatorsContainer: () => ({
              cursor: 'pointer'
            }),
            clearIndicator: (provided: any) => ({
              ...provided,
              padding: '0 6px'
            }),
            valueContainer: (provided: any) => ({
              ...provided,
              padding: '0 12px'
            }),
            dropdownIndicator: () => ({
              display: 'none'
            }),
            indicatorSeparator: () => ({
              display: 'none'
            }),
            menuList: (provided: any) => ({
              ...provided,
              width: '100%',
              '::-webkit-scrollbar': {
                width: '0px',
                height: '0px'
              }
            }),
            menu: (provided: any) => ({
              ...provided,
              width: '100%',
              minWidth: '200px'
            })
          },
          placeholder: placeholder,
          isDisabled: disabled
        }}
      />
    </div>
  )
}

export default AddressAutocomplete
