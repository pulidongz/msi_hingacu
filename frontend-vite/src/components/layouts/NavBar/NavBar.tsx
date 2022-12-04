import { Link } from 'react-router-dom'
import classNames from 'classnames'

import NavItem from '../NavItem'
import styles from './NavBar.module.css'

type NavItemProps = {
  title: string
  path: string
  matches?: (RegExp | string)[]
}

const NavBar = () => {
  const navItems: NavItemProps[] = [
    {
      title: 'About the Project',
      path: '/about-the-project',
      matches: [/\/about-the-project/]
    },
    {
      title: 'Project Partners',
      path: '/project-partners',
      matches: [/\/project-partners/]
    },
    {
      title: 'Data Access',
      path: '/data-access',
      matches: [/\/data-access/]
    },
    {
      title: 'Contact Us',
      path: '/contact-us',
      matches: [/\/contact-us/]
    }
  ]

  return (
    <nav className={styles.navBar}>
      <div className={styles.headerWrapper}>
        <ul className={classNames(styles.navList, styles.isElastic, styles.left)}>
          <NavItem>
            <Link to="/">
              <a className={styles.toolbarButtons}>HINGACU</a>
            </Link>
          </NavItem>
        </ul>

        <ul className={classNames(styles.navList, styles.right)}>
          <>
            {navItems.map(({ title, path, matches = [] }, i) => {
              const currentPath = document.location.pathname
              const isActive = Boolean(
                matches.find(p => (typeof p === 'string' ? p.match(currentPath) : p.test(currentPath)))
              )
              return (
                <NavItem key={i} isActive={isActive}>
                  <Link to={path}>
                    <a className={styles.toolbarButtons}>{title}</a>
                  </Link>
                </NavItem>
              )
            })}
          </>
        </ul>
      </div>
    </nav>
  )
}

export default NavBar
