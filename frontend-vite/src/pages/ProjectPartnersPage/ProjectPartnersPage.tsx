import NavBar from '../../stories/NavBar'

import styles from './ProjectPartnersPage.module.css'

const ProjectPartnersPage = () => {
  return (
    <>
      <NavBar />

      <div className={styles.projectPartnersContainer}>
        <div className={styles.logoRows}>
          <div className={styles.logoContent}>
            <h6 className={styles.agencyTitle}>Funding Agency</h6>
            <img className={styles.agencyLogo} src="/about-the-project/nsc_logo.svg"></img>
            <p className={styles.agencyName}>National Security Council</p>
          </div>
          <div className={styles.logoContent}>
            <h6 className={styles.agencyTitle}>Implementing Agency</h6>
            <img className={styles.agencyLogo} src="/about-the-project/msi_logo.svg"></img>
            <p className={styles.agencyName}>UP Marine Science Institute</p>
          </div>
        </div>

        <h6 className={styles.agencyTitle}>Project Partners</h6>
        <div className={styles.logoRows}>
          <div className={styles.logoContent}>
            <h6 className={styles.agencyTitle}></h6>
            <img className={styles.agencyLogo} src="/about-the-project/pcsd_logo.svg"></img>
            <p className={styles.agencyName}>Palawan Council for Sustainable Development</p>
          </div>
          <div className={styles.logoContent}>
            <img className={styles.agencyLogo} src="/about-the-project/psu_logo.svg"></img>
            <p className={styles.agencyName}>Palawan State University</p>
          </div>
          <div className={styles.logoContent}>
            <h6 className={styles.agencyTitle}></h6>
            <img className={styles.agencyLogo} src="/about-the-project/wpu_logo.svg"></img>
            <p className={styles.agencyName}>Western Philippine University</p>
          </div>
        </div>

        <h6 className={styles.agencyTitle}>Cooperating Faculty Experts</h6>
        <div className={styles.logoRows}>
          <div className={styles.logoContent}>
            <img className={styles.agencyLogo} src="/about-the-project/iesm_logo.svg"></img>
            <p className={styles.agencyName}>Institute of Environmental Science and Meteorology, UP Diliman</p>
          </div>
          <div className={styles.logoContent}>
            <img className={styles.agencyLogo} src="/about-the-project/uplb-ibs_logo.svg"></img>
            <p className={styles.agencyName}>Institute of Biological Sciences, UP Los Baños</p>
          </div>
          <div className={styles.logoContent}>
            <img className={styles.agencyLogo} src="/about-the-project/sesam_logo.svg"></img>
            <p className={styles.agencyName}>School of Environmental Science and Management, UP Los Baños</p>
          </div>
          <div className={styles.logoContent}>
            <img className={styles.agencyLogo} src="/about-the-project/shields_logo.svg"></img>
            <p className={styles.agencyName}>Br. Alfred Shields FSC Ocean Research Center, DLSU</p>
          </div>
        </div>
      </div>
    </>
  )
}

export default ProjectPartnersPage
