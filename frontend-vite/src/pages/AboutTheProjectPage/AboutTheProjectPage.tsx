import NavBar from '../../components/layouts/NavBar'

import styles from './AboutTheProjectPage.module.css'

const AboutTheProjectPage = () => {
  return (
    <>
      <NavBar />
      <div className={styles.aboutTheProjectContainer}>
        <h5 className={styles.title}>About the Project</h5>

        <img className={styles.hingacuLogo} src="/landing/hingacu_logo.svg" alt="Hingacu"></img>

        <p className={styles.hingacuLink}>
          Higher Educational Institution and National Government Agency Capacity Upgrading West Philippine Sea Project
        </p>

        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ac semper non, volutpat nulla. Augue cursus tellus
          cursus amet purus. Nam id sagittis id nunc urna, commodo. Tristique nec hac molestie id risus tortor, ac magna
          faucibus. Posuere sagittis donec feugiat amet, in pulvinar. Adipiscing tempor lobortis quam malesuada nulla
          sagittis, proin massa lectus. Viverra malesuada tellus interdum pellentesque. Scelerisque morbi eget massa
          faucibus eu. Dignissim sapien magna amet ultricies habitasse sagittis morbi. Adipiscing nunc morbi non augue
          enim tellus pharetra est. Hac tellus malesuada nunc in dapibus aliquam convallis vitae. Mattis platea proin
          sit amet tellus vel id facilisis. Phasellus diam fermentum at volutpat at nunc iaculis orci. Et malesuada
          mattis orci, justo gravida non sociis bibendum feugiat. Pretium ut risus faucibus massa velit. Nec fermentum
          rhoncus, eleifend sagittis felis orci sed. Pellentesque scelerisque sit sapien risus. A vestibulum egestas
          cras penatibus commodo, lacus. Libero, mattis diam et mus vulputate pulvinar elit. Est vulputate rhoncus id
          bibendum quis. Eget id et enim, mattis. Et malesuada mattis orci, justo gravida non sociis bibendum feugiat.
          Pretium ut risus faucibus massa velit. Nec fermentum rhoncus, eleifend sagittis felis orci sed. Pellentesque
          scelerisque sit sapien risus. A vestibulum egestas cras penatibus commodo, lacus. Libero, mattis diam et mus
          vulputate pulvinar elit. Est vulputate rhoncus id bibendum quis. Eget id et enim, mattis.
        </p>
      </div>
    </>
  )
}

export default AboutTheProjectPage
