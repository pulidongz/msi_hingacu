import React, { useState } from 'react'
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from 'react-router-dom';

import { makeStyles } from '@mui/styles';
import { ThemeProvider }  from "@mui/styles";
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import InputAdornment from '@mui/material/InputAdornment';
import IconButton from '@mui/material/IconButton';
import Visibility from "@mui/icons-material//Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import PersonOutlineOutlinedIcon from '@mui/icons-material/PersonOutlineOutlined';

import { createTheme } from '@mui/material/styles';

import { useHistory } from 'react-router-dom';

const theme = createTheme();

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="/">
        HINGACU
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function Login (props) {
	let history = useHistory();
	const classes = useStyles();

	const [state, setState] = useState({
    username: "",
    password: "",
  });
  const [loading, setLoading] = useState(false);
	

	const [values, setValues] = React.useState({
    showPassword: false,
  });

	const handleChange = (event) => {
    const { name, value } = event.target;
    setState({ ...state, [name]: value });
  };
  const handleClickShowPassword = () => {
    setValues({ ...values, showPassword: !values.showPassword });
  };
  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

	const login = async (event) => {
    event.preventDefault();
    setLoading(true);
    
    // const { username, password } = state;

    // await dispatch(loginUser(username, password))
    // .then(() => {
    //   setLoading(false);
    //   props.history.push("/");
    //   window.location.reload();
    // })
    // .catch(function (error) {
    //   console.log(error);
    //   setLoading(false);
    // });
  };

	return(
		<Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <PersonOutlineOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Login
        </Typography>

        <form className={classes.form} onSubmit={login}>
          <TextField
            id="username"
            name="username"
            value={state.username}
            onChange={handleChange}
            label="Username"
            variant="outlined"
            margin="normal"
            required
            fullWidth
            type="username"
            autoComplete="username"
            autoFocus
          />
          <TextField
            label="Password"
            id="password"
            name="password"
            value={state.password}
            onChange={handleChange}
            label="Password"
            variant="outlined"
            margin="normal"
            required
            fullWidth
            type={values.showPassword ? 'text' : 'password'}
            autoComplete="current-password"
            InputProps={{
              endAdornment:
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                    edge="end"
                  >
                    {values.showPassword ? <Visibility /> : <VisibilityOff />}
                  </IconButton>
                </InputAdornment>,
            }}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            disabled={loading}
            className={classes.submit}
          >
            {loading && (
                <span className="spinner-border spinner-border-sm"></span>
              )}
            Sign In
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="/forgot-password" variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link href="/signup" variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>

        </form>
      </div>
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
	);
}