import { Link } from 'react-router-dom'
import styles from './NavBar.module.css'

const NavBar = () => {
  return (
    <nav className={styles.navBar}>
      <div className={styles.headerWrapper}>
        <ul>
          <Link to="/">
            <a className={styles.toolbarButtons}>HINGACU</a>
          </Link>
        </ul>
        <ul>
          <Link to="/about-the-project">
            <a className={styles.toolbarButtons}>About the Project</a>
          </Link>
          <Link to="/project-partners">
            <a className={styles.toolbarButtons}>Project Partners</a>
          </Link>
          <Link to="/contact-us">
            <a className={styles.toolbarButtons}>Contact Us</a>
          </Link>
        </ul>
      </div>
    </nav>
  )
}

export default NavBar
