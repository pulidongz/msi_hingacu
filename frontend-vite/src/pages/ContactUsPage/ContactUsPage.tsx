import RoomIcon from '@mui/icons-material/Room'
import LocalPhoneIcon from '@mui/icons-material/LocalPhone'
import EmailIcon from '@mui/icons-material/Email'

import NavBar from '../../stories/NavBar'

import styles from './ContactUsPage.module.css'

const ContactUsPage = () => {
  return (
    <>
      <NavBar />
      <div className={styles.contactUsContainer}>
        <h5 className={styles.title}>Contact Us</h5>
        <p className={styles.subText}>
          Sample text. Click to select the text box. Click again or double click to start editing the text.
        </p>

        <div className={styles.logoContainer}>
          <div className={styles.logoItem}>
            <RoomIcon sx={{ width: '48px', height: '48px' }} />
            <a href="/">Address</a>
          </div>
          <div className={styles.logoItem}>
            <LocalPhoneIcon sx={{ width: '48px', height: '48px' }} />
            <a href="/">Phone</a>
          </div>
          <div className={styles.logoItem}>
            <EmailIcon sx={{ width: '48px', height: '48px' }} />
            <a href="/">Email</a>
          </div>
        </div>
      </div>
    </>
  )
}

export default ContactUsPage
