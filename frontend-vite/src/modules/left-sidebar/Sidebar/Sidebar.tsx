import * as React from 'react'
import { styled, useTheme, Theme, CSSObject } from '@mui/material/styles'
import Box from '@mui/material/Box'
import MuiDrawer from '@mui/material/Drawer'
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar'
import Toolbar from '@mui/material/Toolbar'
import List from '@mui/material/List'
import CssBaseline from '@mui/material/CssBaseline'
import Typography from '@mui/material/Typography'
import Divider from '@mui/material/Divider'
import IconButton from '@mui/material/IconButton'
import ListItem from '@mui/material/ListItem'
import ListItemButton from '@mui/material/ListItemButton'
import ListItemIcon from '@mui/material/ListItemIcon'
import ListItemText from '@mui/material/ListItemText'
import MenuIcon from '@mui/icons-material/Menu'
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft'
import ChevronRightIcon from '@mui/icons-material/ChevronRight'
import InboxIcon from '@mui/icons-material/MoveToInbox'
import MailIcon from '@mui/icons-material/Mail'

import styles from './Sidebar.module.css'
import { useState } from 'react'
import { ExpandLess, ExpandMore, FilterAltOutlined, Search, StarBorder } from '@mui/icons-material'
import { Collapse, Switch, TextField } from '@mui/material'
import { width } from '@mui/system'

const drawerWidth = 240

const openedMixin = (theme: Theme): CSSObject => ({
  width: drawerWidth,
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen
  }),
  overflowX: 'hidden'
})

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen
  }),
  overflowX: 'hidden',
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up('sm')]: {
    width: `calc(${theme.spacing(8)} + 1px)`
  }
})

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'flex-end',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar
}))

interface AppBarProps extends MuiAppBarProps {
  open?: boolean
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: prop => prop !== 'open'
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen
    })
  })
}))

const Drawer = styled(MuiDrawer, { shouldForwardProp: prop => prop !== 'open' })(({ theme, open }) => ({
  width: drawerWidth,
  flexShrink: 0,
  whiteSpace: 'nowrap',
  boxSizing: 'border-box',
  ...(open && {
    ...openedMixin(theme),
    '& .MuiDrawer-paper': openedMixin(theme)
  }),
  ...(!open && {
    ...closedMixin(theme),
    '& .MuiDrawer-paper': closedMixin(theme)
  })
}))

const Sidebar = () => {
  const theme = useTheme()
  const [open, setOpen] = useState(true)
  const [showSpatialFilter, setShowSpatialFilter] = useState(true)
  const [showCoastalIntegrity, setShowCoastalIntegrity] = useState(true)
  const [showMangrove, setShowMangrove] = useState(true)
  const [showSeagrass, setShowSeagrass] = useState(true)
  const [showFish, setShowFish] = useState(true)
  const [showCoral, setShowCoral] = useState(true)

  const handleDrawerOpen = () => {
    setOpen(true)
  }

  const handleDrawerClose = () => {
    setOpen(false)
  }

  // const handleClickListItem = (search) => {
  //   setOpenListItem(prevState => ...prevState, !prevState.search)
  // }

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
            sx={{
              marginRight: 5,
              ...(open && { display: 'none' })
            }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div">
            HINGACU
          </Typography>
        </Toolbar>
      </AppBar>

      <Drawer variant="permanent" open={open}>
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
          </IconButton>
        </DrawerHeader>
        <Divider />
        <List>
          {/* SEARCH */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <img src="/sidebar/search_icon.svg" alt="search_icon" />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Search"
              />
            </ListItemButton>
            <List
              sx={{
                display: open ? 'flex' : 'none'
              }}
              component="div"
              disablePadding
            >
              <ListItemButton sx={{ pl: 4 }}>
                {/* TODO: Replace search input field */}
                <TextField id="standard-basic" label="Standard" variant="standard" />
                {/* <ListItemText primary="Starred" /> */}
              </ListItemButton>
            </List>
          </ListItem>

          {/* SPATIAL FILTER */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
              onClick={() => setShowSpatialFilter(prevState => !prevState)}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <FilterAltOutlined />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Spatial Filter"
              />
              {showSpatialFilter ? (
                <ExpandLess
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              ) : (
                <ExpandMore
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              )}
            </ListItemButton>
            <Collapse
              sx={{
                display: open ? 'flex' : 'none'
              }}
              in={showSpatialFilter}
              timeout="auto"
              unmountOnExit
            >
              <List component="div" disablePadding>
                <ListItemButton>
                  <ListItemText secondary="Station Name" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
                <ListItemButton>
                  <ListItemText sx={{ whiteSpace: 'normal' }} secondary="Marine Biogeographical Region" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
              </List>
            </Collapse>
          </ListItem>

          {/* COASTAL INTEGRITY */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
              onClick={() => setShowCoastalIntegrity(prevState => !prevState)}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <img src="/sidebar/ci_icon.svg" alt="ci_icon" />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Coastal Integrity"
              ></ListItemText>
              {showCoastalIntegrity ? (
                <ExpandLess
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              ) : (
                <ExpandMore
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              )}
            </ListItemButton>
            <Collapse
              sx={{
                display: open ? 'block' : 'none'
              }}
              in={showCoastalIntegrity}
              timeout="auto"
              unmountOnExit
            >
              <List component="div" disablePadding>
                <ListItemButton>
                  <ListItemText secondary="Shoreline Tracing" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
                <ListItemButton>
                  <ListItemText secondary="Beach Profile" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
              </List>
            </Collapse>
          </ListItem>

          {/* MANGROVE */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
              onClick={() => setShowMangrove(prevState => !prevState)}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <img src="/sidebar/mg_icon.svg" alt="mg_icon" />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Mangrove"
              ></ListItemText>
              {showMangrove ? (
                <ExpandLess
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              ) : (
                <ExpandMore
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              )}
            </ListItemButton>
            <Collapse
              sx={{
                display: open ? 'block' : 'none'
              }}
              in={showMangrove}
              timeout="auto"
              unmountOnExit
            >
              <List component="div" disablePadding>
                <ListItemButton>
                  <ListItemText secondary="Area Extent" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
                <ListItemButton>
                  <ListItemText secondary="Species Composition" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
              </List>
            </Collapse>
          </ListItem>

          {/* SEAGRASS */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
              onClick={() => setShowSeagrass(prevState => !prevState)}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <img src="/sidebar/sg_icon.svg" alt="sg_icon" />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Seagrass"
              ></ListItemText>
              {showSeagrass ? (
                <ExpandLess
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              ) : (
                <ExpandMore
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              )}
            </ListItemButton>
            <Collapse
              sx={{
                display: open ? 'block' : 'none'
              }}
              in={showSeagrass}
              timeout="auto"
              unmountOnExit
            >
              <List component="div" disablePadding>
                <ListItemButton>
                  <ListItemText secondary="Area Extent" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
                <ListItemButton>
                  <ListItemText secondary="Species Composition" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
              </List>
            </Collapse>
          </ListItem>

          {/* FISH */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
              onClick={() => setShowFish(prevState => !prevState)}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <img src="/sidebar/fish_icon.svg" alt="fish_icon" />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Fish"
              ></ListItemText>
              {showFish ? (
                <ExpandLess
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              ) : (
                <ExpandMore
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              )}
            </ListItemButton>
            <Collapse
              sx={{
                display: open ? 'block' : 'none'
              }}
              in={showFish}
              timeout="auto"
              unmountOnExit
            >
              <List component="div" disablePadding>
                <ListItemButton>
                  <ListItemText secondary="Level 1" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
                <ListItemButton>
                  <ListItemText secondary="Level 2" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
                <ListItemButton>
                  <ListItemText secondary="Level 3" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
              </List>
            </Collapse>
          </ListItem>

          {/* CORAL */}
          <ListItem disablePadding sx={{ display: 'block' }}>
            <ListItemButton
              sx={{
                minHeight: 48,
                justifyContent: open ? 'initial' : 'center',
                px: 2.5
              }}
              onClick={() => setShowCoral(prevState => !prevState)}
            >
              <ListItemIcon
                sx={{
                  minWidth: 0,
                  mr: open ? 3 : 'auto',
                  justifyContent: 'center',
                  width: 25,
                  height: 25
                }}
              >
                <img src="/sidebar/coral_icon.svg" alt="coral_icon" />
              </ListItemIcon>
              <ListItemText
                sx={{
                  display: open ? 'flex' : 'none'
                }}
                primary="Coral"
              ></ListItemText>
              {showCoral ? (
                <ExpandLess
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              ) : (
                <ExpandMore
                  sx={{
                    display: open ? 'flex' : 'none'
                  }}
                />
              )}
            </ListItemButton>
            <Collapse
              sx={{
                display: open ? 'block' : 'none'
              }}
              in={showCoral}
              timeout="auto"
              unmountOnExit
            >
              <List component="div" disablePadding>
                <ListItemButton>
                  <ListItemText secondary="Hard Coral Classification" />
                  <Switch
                    // checked={state.checkedA}
                    // onChange={handleChange}
                    name="checkedA"
                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                  />
                </ListItemButton>
              </List>
            </Collapse>
          </ListItem>

          {/* {['Search', 'Spatial Filter', 'Coastal Integrity', 'Mangrove', 'Seagrass', 'Fish', 'Coral'].map(
            (text, index) => (
              <ListItem key={text} disablePadding sx={{ display: 'block' }}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? 'initial' : 'center',
                    px: 2.5
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : 'auto',
                      justifyContent: 'center'
                    }}
                  >
                    {index % 2 === 0 ? <InboxIcon /> : <MailIcon />}
                  </ListItemIcon>
                  <ListItemText primary={text} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </ListItem>
            )
          )} */}
        </List>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        <Typography paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
          magna aliqua. Rhoncus dolor purus non enim praesent elementum facilisis leo vel. Risus at ultrices mi tempus
          imperdiet. Semper risus in hendrerit gravida rutrum quisque non tellus. Convallis convallis tellus id interdum
          velit laoreet id donec ultrices. Odio morbi quis commodo odio aenean sed adipiscing. Amet nisl suscipit
          adipiscing bibendum est ultricies integer quis. Cursus euismod quis viverra nibh cras. Metus vulputate eu
          scelerisque felis imperdiet proin fermentum leo. Mauris commodo quis imperdiet massa tincidunt. Cras tincidunt
          lobortis feugiat vivamus at augue. At augue eget arcu dictum varius duis at consectetur lorem. Velit sed
          ullamcorper morbi tincidunt. Lorem donec massa sapien faucibus et molestie ac.
        </Typography>
        <Typography paragraph>
          Consequat mauris nunc congue nisi vitae suscipit. Fringilla est ullamcorper eget nulla facilisi etiam
          dignissim diam. Pulvinar elementum integer enim neque volutpat ac tincidunt. Ornare suspendisse sed nisi lacus
          sed viverra tellus. Purus sit amet volutpat consequat mauris. Elementum eu facilisis sed odio morbi. Euismod
          lacinia at quis risus sed vulputate odio. Morbi tincidunt ornare massa eget egestas purus viverra accumsan in.
          In hendrerit gravida rutrum quisque non tellus orci ac. Pellentesque nec nam aliquam sem et tortor. Habitant
          morbi tristique senectus et. Adipiscing elit duis tristique sollicitudin nibh sit. Ornare aenean euismod
          elementum nisi quis eleifend. Commodo viverra maecenas accumsan lacus vel facilisis. Nulla posuere
          sollicitudin aliquam ultrices sagittis orci a.
        </Typography>
      </Box>
    </Box>
  )
}

export default Sidebar
