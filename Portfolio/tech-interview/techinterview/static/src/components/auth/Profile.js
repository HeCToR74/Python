import React from 'react';
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import { uploadFile } from 'react-s3';
import { withRouter } from 'react-router-dom';
import PasswordChange from 'src/components/auth/PasswordChange'
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Avatar from '@material-ui/core/Avatar';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { config } from 'src/constants.js';


const URL = '/api/user/user/';
const URL1 = '/api/user/profile/';

export class Profile extends React.Component {
  /**
   * * Constructor of class
   * @param{props} props
   */
  constructor(props) {
    super(props);

    this.state = {
      picture: null,
      open: false,

      inputFirst: {
        value: '',
        error: '',
      },
      inputLast: {
        value: '',
        error: '',
      },
      user: {
        id: '',
        login: '',
        first: '',
        last: '',
        email: '',
        role: '',
      },
      avatar: '',
    };

    this.handleClose = this.handleClose.bind(this);
    this.handleOpen = this.handleOpen.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChangeLast = this.handleChangeLast.bind(this);
    this.handleChangeFirst= this.handleChangeFirst.bind(this);
    this.handleNewImage = this.handleNewImage.bind(this);

  };


  componentWillMount(event){
    console.log(this.props);
    axios.get(URL)
        .then((response) => this.setState({
          user: {
            login: response.data.user.login,
            email: response.data.user.email,
            role: response.data.user.role,
          },
          avatar: response.data.user.avatar,
          inputFirst: {
            value: response.data.user.first,
          },
          inputLast: {
            value: response.data.user.last,
          },
        })
)
        .catch((error) => console.log(error));
  };

  handleOpen () {
    this.setState({open: true});
  };

  handleChangeFirst(event) {
    this.setState({
      inputFirst: {
        value: event.target.value,
      },
    });
  };
  handleChangeLast(event) {
    this.setState({
      inputLast: {
        value: event.target.value,
      },
    });
  };

  handleClose() {
    this.setState({open: false});
  };

  handleNewImage(event){
    if (event.target.value !== ''){
      const name = this.state.user.login + // Concat with file extension.
          event.target.files[0].name.substring(event.target.files[0].name.lastIndexOf('.'));
      const file = new File([event.target.files[0]],
        name, { type: event.target.files[0].type });
      this.setState({
        picture: file,
      }, () => {
        console.log(this.state.picture);
      });
    }
  }

  /**
   * handle submit change first name and last name
   * @param{event} event
   *  */
  handleSubmit(event) {

    event.preventDefault();
    if (this.state.picture !== null
    && this.state.inputLast !== ''
    && this.state.inputFirst !== ''){
      uploadFile(this.state.picture, config)
          .then((data) => {
            const userData = {
              avatar: data.location,
              first_name: this.state.inputFirst.value,
              last_name: this.state.inputLast.value,
            };
            axios.put(URL1, userData)
                .then((res) => {
                  this.setState({
                    avatar: data.location,
                    first_name: this.state.inputFirst.value,
                    last_name: this.state.inputLast.value,
                    open: false,
                  });
                })
                .catch((error) => {
                  console.log(error);
                });
          })
          .catch((err) => console.error(err));
    }
    if (this.state.picture !== null){
      uploadFile(this.state.picture, config)
          .then((data) => {
            const userData = {
              avatar: data.location,
            };
            axios.put(URL1, userData)
                .then((res) => {
                  this.setState({
                    avatar: data.location,
                    open: false,
                  });
                })
                .catch((error) => {
                  console.log(error);
                });
          })
          .catch((err) => console.error(err));
    }

    if (this.state.inputLast !== ''
        && this.state.inputFirst !== ''){
      const userData = {
        first_name: this.state.inputFirst.value,
        last_name: this.state.inputLast.value,
      };
      axios.put(URL1, userData)
          .then((res) => {
            this.setState({
              first_name: this.state.inputFirst.value,
              last_name: this.state.inputLast.value,
              open: false,
            });
          })
          .catch((error) => {
            console.log(error);
          });
    }

  };

  /**
   * Render HTML form with handlers
   */
  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <Paper id='Paper' className={classes.root} elevation={20}>
          <form encType="multipart/form-data">
            <br/>
            <h1>  User profile</h1>
            <br/>
            <Avatar alt="you avatar"
                    src={this.state.avatar}
                    className={classes.bigAvatar} />
            <br />
            <input
              accept="image/*"
              id="text-button-file"
              multiple
              className={classes.inputFile}
              type="file"
              onChange={this.handleNewImage}
            />
            <label htmlFor="text-button-file">
              <Button component="span"
                      className={classes.button}
                      color='primary'>
                Upload new image
              </Button>
            </label>
            <br/>
            <br/>
            <TextField
              id='email'
              onChange={this.handleChangePassword}
              value={this.state.user.email}
              type = "text" 
              helperText='Input new email'
              className={classes.textField}
              disabled='true'
            />
            <br/><br/>
            <TextField
              id='firstName'
              name="first"
              type = "text"
              onChange={this.handleChangeFirst}
              placeholder={this.state.inputFirst.value}
              helperText='Input new first name'
              className={classes.textField}
            />
            <br/><br/>
            <TextField
              id='lastName'
              name="last"
              onChange={this.handleChangeLast}
              type = "text"
              placeholder = {this.state.inputLast.value}
              helperText='Input new last name'
              className={classes.textField}
            />
            <br/><br/>
            <Button 
              id='saveChanges'
              variant='contained'
              className={classes.button}
              onClick={this.handleOpen}
              color='primary' >
              Save changes
            </Button>
            <br/>
            <Dialog
              open={this.state.open}
              onClose={this.handleClose} >
              <DialogTitle id='DialogTitle'>
              </DialogTitle>
              <DialogContent>
                <DialogContentText>
                  Are you sure you really want to change your name?
                </DialogContentText>
              </DialogContent>
              <DialogActions>
                <Button
                  onClick={this.handleClose}
                  color="primary" >
                  Cancel
                </Button>
                <Button
                  onClick={this.handleSubmit}
                  color="primary"
                  autoFocus >
                  Submit
                </Button>
              </DialogActions>
            </Dialog>

            <PasswordChange />
            <br />
            <br />
          </form>
        </Paper>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(Profile));
