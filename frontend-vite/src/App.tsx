import { Suspense, lazy } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'

const Login = lazy(() => import('./modules/auth/Login'))
const Signup = lazy(() => import('./modules/auth/Signup'))
const ForgotPassword = lazy(() => import('./modules/auth/ForgotPassword'))
const ResetPassword = lazy(() => import('./modules/auth/ResetPassword'))

const Home = lazy(() => import('./pages/Home'))


function App() {
  return (
    <Router>
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            <Route  path="/" element={<Home />}/>
            <Route path="login" element={<Login />}/>
            <Route path="signup" element={<Signup />}/>
            <Route path="forgot-password" element={<ForgotPassword />}/>
            <Route path="reset-password" element={<ResetPassword />}/>

            {/* <Route exact path="/dashboard" component={Dashboard}/>
            <Route exact path="/home" component={Home}/>

            <Route component={Error404} /> */}
          </Routes>
        </Suspense>
      </Router>
  )
}

export default App
