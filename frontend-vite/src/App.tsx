import { Suspense, lazy } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import '../styles/globals.css'
import '../styles/variables.css'
import '../styles/typeography.css'

// import './App.css'

const Login = lazy(() => import('./modules/auth/Login'))
const Signup = lazy(() => import('./modules/auth/Signup'))
const ForgotPassword = lazy(() => import('./modules/auth/ForgotPassword'))
const ResetPassword = lazy(() => import('./modules/auth/ResetPassword'))

const HomePage = lazy(() => import('./pages/HomePage'))
const LandingPage = lazy(() => import('./pages/LandingPage/LandingPage.js'))

const App = () => {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="login" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route path="forgot-password" element={<ForgotPassword />} />
          <Route path="reset-password" element={<ResetPassword />} />

          {/* <Route exact path="/dashboard" component={Dashboard}/>
            <Route exact path="/home" component={Home}/>

            <Route component={Error404} /> */}
        </Routes>
      </Suspense>
    </Router>
  )
}

export default App
