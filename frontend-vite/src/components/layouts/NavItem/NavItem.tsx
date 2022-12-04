import classNames from 'classnames'
import styles from './NavItem.module.css'

type NavItemProps = {
  className?: string
  children?: React.ReactNode
  disabled?: boolean
  isActive?: boolean
  isPrimary?: boolean
  onClick?: () => void
}

const NavItem = ({ className, children, disabled, isActive, isPrimary, onClick }: NavItemProps) => {
  return (
    <li
      className={classNames(
        styles.navItem,
        {
          [styles.disabled]: disabled,
          [styles.isPrimary]: isPrimary,
          [styles.isActive]: isActive
        },
        className
      )}
      onClick={onClick}
    >
      {children}
    </li>
  )
}

export default NavItem
