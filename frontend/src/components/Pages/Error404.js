import React, { useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { ThemeProvider }  from "@material-ui/core/styles";
import Grid from '@material-ui/core/Grid';
import Fab from '@material-ui/core/Fab';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import InputAdornment from '@material-ui/core/InputAdornment';
import IconButton from '@material-ui/core/IconButton';
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import Box from '@material-ui/core/Box';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';

import createMuiTheme from "@material-ui/core/styles/createMuiTheme";

import { useHistory } from 'react-router-dom';

const theme = createMuiTheme();

export default function Error404 () {
	let history = useHistory();

	return(<Typography>Error404</Typography>);
}