import React from 'react';
import axios from "axios/index";
import {withRouter} from 'react-router-dom';
import OutsideClickHandler from 'react-outside-click-handler';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles/index';
import Drawer from '@material-ui/core/Drawer/index';
import CssBaseline from '@material-ui/core/CssBaseline/index';
import AppBar from '@material-ui/core/AppBar/index';
import Toolbar from '@material-ui/core/Toolbar/index';
import List from '@material-ui/core/List/index';
import Typography from '@material-ui/core/Typography/index';
import Divider from '@material-ui/core/Divider/index';
import IconButton from '@material-ui/core/IconButton/index';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import MenuItem from '@material-ui/core/MenuItem/index';
import Button from '@material-ui/core/Button';
import UserInfo from "./UserInfo";


const URL = '/api/user/user/';

export class Header extends React.Component {
    constructor(props) {
    super(props);

    this.state = {
       open: false,
       title: 'Home',
       role: '',
    };
  };

  handleDrawerOpen(){
      if(this.state.role=='expert' || this.state.role=='candidate') {
          this.setState({open: false});
      }
       else {
           return this.setState({ open: true });
      }
  };

  handleDrawerClose (){
    return this.setState({ open: false });
  };

  handleSubmit(e) {
    const headers = {'Content-Type': 'application/json'};
    e.preventDefault();
    axios.post('/api/user/logout/', {headers, body: '', method: 'POST'})
        .then((res) => {
          document.location.replace('/login/');
          console.log(res.data);
          this.setState({
            snackbar: {
              message: 'Logged out',
              open: true,
            },
          });
        });
  };
  componentDidUpdate(prevProps, prevState) {
    if (this.state.role == '') {
        axios
            .get(URL)
            .then((response) => {
                this.setState({
                    role: response.data.user.role,
                });
            })
            .catch((error) => console.log(error));
    }
  };

    componentDidMount() {
        this.componentDidUpdate();
        const {pathname} = this.props.location;
        const namePage = pathname.split('/')[1];
        let title = namePage.charAt(0).toUpperCase()+namePage.slice(1, namePage.length);
        this.setState({title})
    }

    render()
    {
        const { classes } = this.props;
        const {title} = this.state;
        return (
         <OutsideClickHandler
        onOutsideClick={this.handleDrawerClose.bind(this)}
        >
      <div>
        <CssBaseline />
        <AppBar
          id="appbar"
          position="fixed"
        >
          <Toolbar disableGutters={true}>
            <IconButton
              color="inherit"
              aria-label="Open drawer"
              onClick={this.handleDrawerOpen.bind(this)}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" color="inherit" noWrap>
                {title}
            </Typography>
              <Button
                  onClick={this.handleSubmit.bind(this)}
                  color="inherit"
                  type="submit"
                  style={{position: 'absolute', right: 20}}
              >Logout
              </Button>
          </Toolbar>
        </AppBar>
          <Drawer
          anchor="left"
          open={this.state.open}
          id="drawer"
          >
          <div>
            <IconButton onClick={this.handleDrawerClose.bind(this)}>
              <ChevronLeftIcon />
            </IconButton>
          </div>
          <Divider />
          <UserInfo/>
          <List className={classes.sidebarlist }>

                  <Button href='/home/'
                  className={classes.sidebarButton}>
                      Home
                  </Button>

                  <Button href='/profile/'
                  className={classes.sidebarButton}>
                      Manage Profile
                  </Button>

                  <Button href='/section/'
                  className={classes.sidebarButton}>
                      Sections
                  </Button>

                  <Button href='/stage/'
                  className={classes.sidebarButton}>
                      Stages
                  </Button>

                  <Button href='/question/'
                  className={classes.sidebarButton}>
                      Questions
                  </Button>

                  <Button href='/department/'
                  className={classes.sidebarButton}>
                      Departments
                  </Button>

                  <Button href='/grade/'
                  className={classes.sidebarButton}>
                      Grades
                  </Button>

                  <Button href='/interview/'
                  className={classes.sidebarButton}>
                      Interviews
                  </Button>

                  <Button href='/analytics/'
                  className={classes.sidebarButton}>
                      Analytics
                  </Button>

          <Divider />
          </List>
        </Drawer>
      </div>
  </OutsideClickHandler>
    );
  }
}

export default withStyles(styles)(withRouter(Header));
