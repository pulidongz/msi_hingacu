import { Suspense, lazy } from 'react'

import styles from './Home.module.css'

const Sidebar = lazy(() => import('../../modules/left-sidebar/Sidebar'))
const RSidebar = lazy(() => import('../../modules/right-sidebar/RSidebar'))


const Home = () => {
	return(
		<>
		<Sidebar />
		<RSidebar />
		</>
		
	)
}

export default Home