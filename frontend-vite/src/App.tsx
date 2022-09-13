import { Suspense, lazy } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'

const Login = lazy(() => import('./modules/auth/Login'))




function App() {
  return (
    <Router>
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            {/* <Route exact path="/" component={Home}/> */}
            <Route path="login" element={<Login />}/>
            {/* <Route exact path="/signup" component={SignUp}/>
            <Route exact path="/forgot-password" component={ForgotPassword}/>
            <Route exact path="/reset-password" component={ResetPassword}/>

            <Route exact path="/dashboard" component={Dashboard}/>
            <Route exact path="/home" component={Home}/>

            <Route component={Error404} /> */}
          </Routes>
        </Suspense>
      </Router>
  )
}

export default App
