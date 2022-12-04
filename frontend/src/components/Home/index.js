import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
import { Card, CardMedia, Checkbox } from '@mui/material';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircle from '@mui/icons-material/AccountCircle';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListItemButton from '@mui/material/ListItemButton';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import MailIcon from '@mui/icons-material/Mail';
import HomeIcon from '@mui/icons-material/Home';
import LocationSearchingIcon from '@mui/icons-material/LocationSearching';
import HelpIcon from '@mui/icons-material/Info';
import InfoIcon from '@mui/icons-material/Help';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import Collapse from '@mui/material/Collapse';
import PublicIcon from '@mui/icons-material/Public';
import MapIcon from '@mui/icons-material/Map';
import {Link} from 'react-router-dom';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';

import SiteEcoTabs from './SiteEcoTabs';
import NavMenu from './NavMenu';
import SiteEcosystems from './SiteEcosystems';
import SiteSearchDialog from './SiteSearchDialog';
import SearchDialog from './SearchDialog';
import HomeMap from './HomeMap';
import MapOptions from './MapOptions';
import GeoSearch from './GeoSearch';
import LonLatSearch from './LonLatSearch';

const drawerWidth = 365;

const Main = styled('main', { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    flexGrow: 1,
    padding: theme.spacing(3),
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: `-${drawerWidth}px`,
    ...(open && {
      transition: theme.transitions.create('margin', {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
      marginLeft: 0,
    }),
  }),
);

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme, open }) => ({
  transition: theme.transitions.create(['margin', 'width'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: `${drawerWidth}px`,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));

export default function Home() {
  const theme = useTheme();
  const [open, setOpen] = React.useState(true);
  const [auth, setAuth] = React.useState(true);
  const [anchorEl, setAnchorEl] = React.useState(null);

  const [openMangrove, setOpenMangrove] = React.useState(false);
  const [openSeagrass, setOpenSeagrass] = React.useState(false);
  const [openCoastal, setOpenCoastal] = React.useState(false);
  const [openReef, setOpenReef] = React.useState(false);
  const [openFish, setOpenFish] = React.useState(false);

  const [habitat, setChecked] = React.useState({
    mangrove: true,
    seagrass: true,
    coastal: true,
    reef: true,
    fish: true,
  });

  const {mangrove, seagrass, coastal, reef, fish} = habitat;

  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleDropdown = (value) => {
    switch (value) {
      case 'mangrove':
        setOpenMangrove(!openMangrove);
        break;
      case 'seagrass':
        setOpenSeagrass(!openSeagrass);
        break;
      case 'coastal':
        setOpenCoastal(!openCoastal);
        break;
      case 'reef':
        setOpenReef(!openReef);
        break;
      case 'fish':
        setOpenFish(!openFish);
        break;
    }
  }

  const handleCheckbox = (event) => {
    setChecked({ ...habitat, 
      [event.target.name]: event.target.checked });
  }

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar position="fixed" open={open}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            sx={{ mr: 2, ...(open && { display: 'none' }) }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
            HINGACU
          </Typography>
          {auth && (
            <div>
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleMenu}
                color="inherit"
              >
                <AccountCircle />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorEl}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorEl)}
                onClose={handleClose}
              >
                <MenuItem onClick={handleClose}><Link to="/login">Login</Link></MenuItem>
                <MenuItem onClick={handleClose}>My account</MenuItem>
              </Menu>
            </div>
          )}
        </Toolbar>
      </AppBar>
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
          },
        }}
        variant="persistent"
        anchor="left"
        open={open}
      >
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
          </IconButton>
        </DrawerHeader>
        <Divider />

        <List dense={false}>
          <ListItem>
            <Paper elevation={3} style={{backgroundColor: "#F1F0EE",  width: 330}}>
              <Grid container spacing={2} direction="column" justifyContent="center" alignItems="center" style={{padding: 15}}>
                <Grid item xs={12}>
                <Typography variant="button" display="block" gutterBottom>
                  Location Tools
                </Typography>
                </Grid>
                <Grid item xs={12}>
                  <GeoSearch />
                </Grid>
                <Grid item xs={12}>
                  <LonLatSearch />
                </Grid>
              </Grid>       
            </Paper>
          </ListItem>

          {/* MANGROVE */}
          <ListItem>
            <Paper elevation={3} style={{backgroundColor: "#F1F0EE",  width: 330}}>
              <Grid container spacing={2} direction="row" justifyContent="center" alignItems="center" style={{padding: 15}}>
                <Grid item xs={2}>
                  <Checkbox
                    name="mangrove"
                    edge="start"
                    checked={mangrove}
                    disableRipple
                    color="primary"
                    onChange={handleCheckbox}
                  />
                </Grid>
                <Grid item xs={8}>
                  <Typography variant="button" display="block" gutterBottom>Mangrove</Typography>
                </Grid>
                <Grid item xs={2}>
                  <ListItemButton onClick={(e) => handleDropdown("mangrove")}>
                    {openMangrove ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </Grid>
                <Collapse in={openMangrove} timeout="auto" unmountOnExit>
                  <List dense={true} component="div" disablePadding>
                    <ListItem sx={{ pl: 2 }}>
                      <Typography variant="body2" color="textSecondary">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                      </Typography>
                    </ListItem>
                  </List>
                </Collapse>
              </Grid>
            </Paper>
          </ListItem>

          {/* SEAGRASS */}
          <ListItem>
            <Paper elevation={3} style={{backgroundColor: "#F1F0EE",  width: 330}}>
              <Grid container spacing={2} direction="row" justifyContent="center" alignItems="center" style={{padding: 15}}>
                <Grid item xs={2}>
                  <Checkbox
                    name="seagrass"
                    edge="start"
                    checked={seagrass}
                    disableRipple
                    color="primary"
                    onChange={handleCheckbox}
                  />
                </Grid>
                <Grid item xs={8}>
                  <Typography variant="button" display="block" gutterBottom>Seagrass</Typography>
                </Grid>
                <Grid item xs={2}>
                  <ListItemButton onClick={(e) => handleDropdown("seagrass")}>
                    {openSeagrass ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </Grid>
                <Collapse in={openSeagrass} timeout="auto" unmountOnExit>
                  <List dense={true} component="div" disablePadding>
                    <ListItem sx={{ pl: 2 }}>
                      <Typography variant="body2" color="textSecondary">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                      </Typography>
                    </ListItem>
                  </List>
                </Collapse>
              </Grid>
            </Paper>
          </ListItem>
          
          {/* COASTAL INTEGRITY */}
          <ListItem>
            <Paper elevation={3} style={{backgroundColor: "#F1F0EE",  width: 330}}>
              <Grid container spacing={2} direction="row" justifyContent="center" alignItems="center" style={{padding: 15}}>
                <Grid item xs={2}>
                  <Checkbox
                    name="coastal"
                    edge="start"
                    checked={coastal}
                    disableRipple
                    color="primary"
                    onChange={handleCheckbox}
                  />
                </Grid>
                <Grid item xs={8}>
                  <Typography variant="button" display="block" gutterBottom>Coastal Integrity</Typography>
                </Grid>
                <Grid item xs={2}>
                  <ListItemButton onClick={(e) => handleDropdown("coastal")}>
                    {openSeagrass ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </Grid>
                <Collapse in={openCoastal} timeout="auto" unmountOnExit>
                  <List dense={true} component="div" disablePadding>
                    <ListItem sx={{ pl: 2 }}>
                      <Typography variant="body2" color="textSecondary">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                      </Typography>
                    </ListItem>
                  </List>
                </Collapse>
              </Grid>
            </Paper>
          </ListItem>

          {/* CORAL REEF */}
          <ListItem>
            <Paper elevation={3} style={{backgroundColor: "#F1F0EE",  width: 330}}>
              <Grid container spacing={2} direction="row" justifyContent="center" alignItems="center" style={{padding: 15}}>
                <Grid item xs={2}>
                  <Checkbox
                    name="reef"
                    edge="start"
                    checked={reef}
                    disableRipple
                    color="primary"
                    onChange={handleCheckbox}
                  />
                </Grid>
                <Grid item xs={8}>
                  <Typography variant="button" display="block" gutterBottom>Reef</Typography>
                </Grid>
                <Grid item xs={2}>
                  <ListItemButton onClick={(e) => handleDropdown("reef")}>
                    {openSeagrass ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </Grid>
                <Collapse in={openReef} timeout="auto" unmountOnExit>
                  <List dense={true} component="div" disablePadding>
                    <ListItem sx={{ pl: 2 }}>
                      <Typography variant="body2" color="textSecondary">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                      </Typography>
                    </ListItem>
                  </List>
                </Collapse>
              </Grid>
            </Paper>
          </ListItem>

          {/* FISH */}
          <ListItem>
            <Paper elevation={3} style={{backgroundColor: "#F1F0EE",  width: 330}}>
              <Grid container spacing={2} direction="row" justifyContent="center" alignItems="center" style={{padding: 15}}>
                <Grid item xs={2}>
                  <Checkbox
                    name="fish"
                    edge="start"
                    checked={fish}
                    disableRipple
                    color="primary"
                    onChange={handleCheckbox}
                  />
                </Grid>
                <Grid item xs={8}>
                  <Typography variant="button" display="block" gutterBottom>Fish</Typography>
                </Grid>
                <Grid item xs={2}>
                  <ListItemButton onClick={(e) => handleDropdown("fish")}>
                    {openSeagrass ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </Grid>
                <Collapse in={openFish} timeout="auto" unmountOnExit>
                  <List dense={true} component="div" disablePadding>
                    <ListItem sx={{ pl: 2 }}>
                      <Typography variant="body2" color="textSecondary">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                        sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                      </Typography>
                    </ListItem>
                  </List>
                </Collapse>
              </Grid>
            </Paper>
          </ListItem>
        </List>
      </Drawer>
      <Main open={open} sx={{flexGrow: 1, p: 0}}>
        <DrawerHeader />
        <HomeMap />
      </Main>
    </Box>
  );
}