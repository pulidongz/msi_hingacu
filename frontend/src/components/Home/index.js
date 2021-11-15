import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
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

import SiteEcoTabs from './SiteEcoTabs';
import NavMenu from './NavMenu';
import SiteEcosystems from './SiteEcosystems';
import SiteSearchDialog from './SiteSearchDialog';
import SearchDialog from './SearchDialog';
import HomeMap from './HomeMap';
import MapOptions from './MapOptions';

const drawerWidth = 400;

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

  const [openHome, setOpenHome] = React.useState(false);
  const [openMapOptions, setOpenMapOptions] = React.useState(true);
  const [openSiteSelect, setOpenSiteSelect] = React.useState(true);
  const [openHabitat, setOpenHabitat] = React.useState(true);
  const [openAbout, setOpenAbout] = React.useState(false);
  const [openInfo, setOpenInfo] = React.useState(false);

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

  const handleClickHome = () => {
    setOpenHome(!openHome);
  };
  const handleClickMapOptions = () => {
    setOpenMapOptions(!openMapOptions);
  };
  const handleClickSiteSelect = () => {
    setOpenSiteSelect(!openSiteSelect);
  };
  const handleClickHabitat = () => {
    setOpenHabitat(!openHabitat);
  };
  const handleClickAbout = () => {
    setOpenAbout(!openAbout);
  };
  const handleClickInfo = () => {
    setOpenInfo(!openInfo);
  };

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
            Hingacu
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
        <List dense={true}>

          {/* ***HOME*** */}
          <ListItemButton onClick={handleClickHome}>
            <ListItemIcon>
							<HomeIcon />
						</ListItemIcon>
						<ListItemText primary="Home" />
            {openHome ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={openHome} timeout="auto" unmountOnExit>
            <List dense={true} component="div" disablePadding>
              <ListItemButton sx={{ pl: 2 }}>
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
              </ListItemButton>
            </List>
          </Collapse>

          {/* ***MAP OPTIONS*** */}
          <ListItemButton onClick={handleClickMapOptions}>
            <ListItemIcon>
							<MapIcon />
						</ListItemIcon>
						<ListItemText primary="Map Options" />
            {openMapOptions ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={openMapOptions} timeout="auto" unmountOnExit>
            <List dense={true} component="div">
              <ListItem sx={{ pl: 5 }}>
                <MapOptions />
              </ListItem>
            </List>
          </Collapse>

          {/* ***SITE SELECT*** */}
          <ListItemButton onClick={handleClickSiteSelect}>
            <ListItemIcon>
							<LocationSearchingIcon />
						</ListItemIcon>
						<ListItemText primary="Site Selection" />
            {openSiteSelect ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={openSiteSelect} timeout="auto" unmountOnExit>
            <List dense={true} component="div">
              <ListItem sx={{ pl: 5 }}>
                <SearchDialog />
              </ListItem>
            </List>
          </Collapse>

          {/* ***HABITAT*** */} 
          <ListItemButton onClick={handleClickHabitat}>
            <ListItemIcon>
							<PublicIcon />
						</ListItemIcon>
						<ListItemText primary="Habitat" />
            {openHabitat ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={openHabitat} timeout="auto" unmountOnExit>
            <List dense={true} component="div" disablePadding>
              <ListItem sx={{ pl: 2 }}>
                <SiteEcosystems />
                {/* <SiteEcoTabs /> */}
              </ListItem>
            </List>
          </Collapse>

          {/* ***ABOUT*** */}
          <ListItemButton onClick={handleClickAbout}>
            <ListItemIcon>
							<HelpIcon />
						</ListItemIcon>
						<ListItemText primary="About" />
            {openAbout ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={openAbout} timeout="auto" unmountOnExit>
            <List dense={true} component="div" disablePadding>
              <ListItemButton sx={{ pl: 2 }}>
                <Typography variant="body2" color="textSecondary">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                </Typography>
              </ListItemButton>
            </List>
          </Collapse>

          {/* ***INFO*** */}
          <ListItemButton onClick={handleClickInfo}>
            <ListItemIcon>
							<InfoIcon />
						</ListItemIcon>
						<ListItemText primary="Info" />
            {openInfo ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={openInfo} timeout="auto" unmountOnExit>
            <List dense={true} component="div" disablePadding>
              <ListItemButton sx={{ pl: 2 }}>
                <Typography variant="body2" color="textSecondary">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                </Typography>
              </ListItemButton>
            </List>
          </Collapse>
        </List>
      </Drawer>
      <Main open={open} sx={{flexGrow: 1, p: 0}}>
        <DrawerHeader />
        <HomeMap />
      </Main>
    </Box>
  );
}