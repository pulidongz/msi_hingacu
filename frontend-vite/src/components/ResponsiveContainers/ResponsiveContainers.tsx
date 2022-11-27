import React from 'react'
import classNames from 'classnames'
import styles from './ResponsiveContainers.module.css'

type Props = {
  children?: React.ReactNode
  className?: string
}

/* Row containers */

const SlimContainer = ({ children, className, ...props }: Props) => (
  <div className={classNames(styles.slim, className)} {...props}>
    {children}
  </div>
)

const RegularContainer = ({ children, className, ...props }: Props) => (
  <div className={classNames(styles.regular, className)} {...props}>
    {children}
  </div>
)

const WideContainer = ({ children, className, ...props }: Props) => (
  <div className={classNames(styles.wide, className)} {...props}>
    {children}
  </div>
)

const Panel = ({ children, className, ...props }: Props) => (
  <div className={classNames(styles.panel, className)} {...props}>
    {children}
  </div>
)

const PageContainer = ({ children, className, ...props }: Props) => (
  <RegularContainer className={classNames(styles.page, className)} {...props}>
    {children}
  </RegularContainer>
)

export { SlimContainer, RegularContainer, WideContainer, Panel, PageContainer }
