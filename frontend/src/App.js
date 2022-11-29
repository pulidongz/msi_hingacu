import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';

// Lazy imports
const Login = lazy(() => import('./components/Accounts/Login'));
const SignUp = lazy(() => import('./components/Accounts/SignUp'));
const ForgotPassword = lazy(() => import('./components/Accounts/ForgotPassword'));
const ResetPassword = lazy(() => import('./components/Accounts/ResetPassword'));

const Dashboard = lazy(() => import('./components/Dashboard'));
const Home = lazy(() => import('./components/Home'));

const Error404 = lazy(() => import('./components/Pages/Error404'));

const theme = createTheme({
  palette: {
    primary: {
      main: '#286D99',
    },
    secondary: {
      main: '#E59036',
    },
  },
});


function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Suspense fallback={<div>Loading...</div>}>
          <Switch>
            <Route exact path="/" component={Home}/>
            <Route exact path="/login" component={Login}/>
            <Route exact path="/signup" component={SignUp}/>
            <Route exact path="/forgot-password" component={ForgotPassword}/>
            <Route exact path="/reset-password" component={ResetPassword}/>

            <Route exact path="/dashboard" component={Dashboard}/>
            <Route exact path="/home" component={Home}/>

            <Route component={Error404} />
          </Switch>
        </Suspense>
      </Router>
    </ThemeProvider>
  );
}

export default App;
