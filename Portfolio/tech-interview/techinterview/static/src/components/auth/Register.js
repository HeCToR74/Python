/* eslint max-len: ["error", { "ignoreRegExpLiterals": true }]*/

import React from 'react';
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import { withRouter, Redirect, Link } from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Snackbar from '@material-ui/core/Snackbar';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { expRegPass, expRegEmail } from 'src/constants.js';


const regURL = '/api/user/registration/';
const confURL = '/api/user/verify-email/';

/**
 * Creates a form to create new user
 */
export class Register extends React.Component {
  /**
   * Constructor of class
   * @param {*} props - props from parent object
   */
  constructor(props) {
    super(props);

    this.state = {

      inputLogin: { value: '', error: false, label: ' ' },
      inputPass: { value: '', error: false, label: ' ' },
      inputConfirm: { value: '', error: false, label: ' ' },
      inputFirst: { value: '', error: false, label: ' ' },
      inputLast: { value: '', error: false, label: ' ' },
      inputEmail: { value: '', error: false, label: ' ' },

      snackbarMessage: {
        open: false,
        message: '',
      },

      dialogMessage: {
        open: false,
      },
    };
  };

  /**
   * Change handler for inputLogin
   * @param {*} event - current event
   */
  handleChangeLogin(event) {
    if (event.target.value === '') {
      this.setState({
        inputLogin: {
          error: true,
          label: 'Login can\'t be empty',
        }
      });
    } else {
      this.setState({
        inputLogin: {
          value: event.target.value,
          error: false,
          label: ' ',
        }
      });
    }
  };

  /**
   * Change handler for inputPass
   * @param {*} event - current event
   */
  handleChangePassword(event) {
    if (event.target.value === '') {
      this.setState({
        inputPass: {
          error: true,
          label: 'Password can\'t be empty',
        }
      });
    } else {
      if (expRegPass.test(event.target.value)) {
        this.setState({
          inputPass: {
            value: event.target.value,
            error: false,
            label: ' ',
          },
        });
      } else {
        this.setState({
          inputPass: {
            value: event.target.value,
            error: true,
            label: 'Password isn\'t valid. Ex: qwe123Q!',
          },
        });
      }
      expRegPass.test(event.target.value);
    }
    if (this.state.inputConfirm.value !== '') {
      this.setState({
        inputConfirm: {
          value: this.state.inputConfirm.value,
          error: event.target.value !== this.state.inputConfirm.value ?
            true : false,
          label: event.target.value !== this.state.inputConfirm.value ?
            'Passwords do not match' : ' ',
        },
      });
    }
  };

  /**
   * Change handler for inputConfirm
   * @param {*} event - current event
   */
  handleChangeConfirm(event) {
    this.setState({
      inputConfirm: {
        value: event.target.value,
        error: event.target.value !== this.state.inputPass.value ?
          true : false,
        label: event.target.value !== this.state.inputPass.value ?
          'Passwords do not match' : ' ',
      },
    });
  };

  /**
   * Change handler for inputFirst
   * @param {*} event - current event
   */
  handleChangeFirstName(event) {
    if (event.target.value === '') {
      this.setState({
        inputFirst: {
          error: true,
          label: 'Field can\'t be empty',
        }
      });
    } else {
      this.setState({
        inputFirst: {
          value: event.target.value,
          error: false,
          label: ' ',
        }
      });
    }
  };

  /**
   * Change handler for inputLast
   * @param {*} event - current event
   */
  handleChangeLastName(event) {
    if (event.target.value === '') {
      this.setState({
        inputLast: {
          error: true,
          label: 'Field can\'t be empty',
        }
      });
    } else {
      this.setState({
        inputLast: {
          value: event.target.value,
          error: false,
          label: ' ',
        }
      });
    }
  };

  /**
   * Change handler for inputEmail
   * @param {*} event - current event
   */
  handleChangeEmail(event) {
    if (event.target.value !== '') {
      if (expRegEmail.test(event.target.value)) {
        expRegEmail.test(event.target.value);
        this.setState({
          inputEmail: {
            value: event.target.value,
            error: false,
            label: ' ',
          }
        });
      } else {
        this.setState({
          inputEmail: {
            value: event.target.value,
            error: true,
            label: 'Email is not valid. Ex: "user@mail.com"',
          },
        });
      }
    } else {
      this.setState({
        inputEmail: {
          error: true,
          label: 'Email can\'t be empty'
        }
      });
    }
  };

  /**
   * Submit handler to send data to API and show message
   * @param {*} event - current event
   */
  handleSubmit(event) {
    event.preventDefault();

    const json = {
      username: this.state.inputLogin.value,
      password1: this.state.inputPass.value,
      password2: this.state.inputConfirm.value,
      first_name: this.state.inputFirst.value,
      last_name: this.state.inputLast.value,
      email: this.state.inputEmail.value,
    };

    axios.post(regURL, json)
      .then((response) => {
        this.setState({
          inputLogin: { value: '', error: false, label: ' ' },
          inputPass: { value: '', error: false, label: ' ' },
          inputConfirm: { value: '', error: false, label: ' ' },
          inputFirst: { value: '', error: false, label: ' ' },
          inputLast: { value: '', error: false, label: ' ' },
          inputEmail: { value: '', error: false, label: ' ' },

          dialogMessage: {
            open: true,
          },
        });
      })
      .catch((error) => {
        console.log(error);
        if (error.response.status == 409) {
          this.setState({
            snackbarMessage: {
              message: error.response.data.message,
              open: true,
              autoHideDuration: 4000,
            },
            inputLogin: {
              value: this.state.inputLogin.value,
              error: error.response.data.error == 'LOGIN' ?
                true : false,
              label: error.response.data.error == 'LOGIN' ?
                'Login is already exist' : ' ',
            },
            inputEmail: {
              value: this.state.inputEmail.value,
              error: error.response.data.error == 'EMAIL' ?
                true : false,
              label: error.response.data.error == 'EMAIL' ?
                'Email is already exist' : ' ',
            },
          });
        } else {
          this.setState({
            snackbarMessage: {
              message: 'User was NOT created',
              open: true,
              autoHideDuration: 4000,
            },
          });
        }
      });
  };

  /**
   * Validation our form and set enabled button
   * @return {*} bool
   */
  setEnabledButton() {
    if (this.state.inputLogin.value !== ''
      && this.state.inputLogin.error === false
      && this.state.inputPass.value !== ''
      && this.state.inputPass.error === false
      && this.state.inputConfirm.value !== ''
      && this.state.inputConfirm.error === false
      && this.state.inputFirst.value !== ''
      && this.state.inputFirst.error === false
      && this.state.inputLast.value !== ''
      && this.state.inputLast.error === false
      && this.state.inputEmail.value !== ''
      && this.state.inputEmail.error === false) {
      return false;
    } else {
      return true;
    }
  };

  /**
   * Open dialog window
   */
  handleOpenDialog() {
    this.setState({ dialogMessage: { open: true } });
  };

  /**
   * Close dialog window and redirect to /login/
   * @param {*} event - current event
   */
  handleCloseDialog(event) {
    event.preventDefault();

    this.setState({ dialogMessage: { open: false } });
    this.props.history.push('/login/');

  };

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({ snackbarMessage: { open: false } });
  }

  /**
   * Render HTML form with handlers
   * @return {*} - Render form to page
   */
  render() {
    const { classes } = this.props;
    return (
      <Paper id='Paper' className={classes.root} elevation={20}>
        <form onSubmit={this.handleSubmit.bind(this)}>
          <h3 className={classes.labelField}>Login:</h3>
          <TextField
            id='login'
            value={this.state.inputLogin.value}
            error={this.state.inputLogin.error}
            label={this.state.inputLogin.label}
            helperText="Input login new user"
            className={classes.textField}
            onChange={this.handleChangeLogin.bind(this)} />
          <h3 className={classes.labelField}>Password:</h3>
          <TextField
            id='password'
            value={this.state.inputPass.value}
            error={this.state.inputPass.error}
            label={this.state.inputPass.label}
            helperText="Input password"
            type="password"
            className={classes.textField}
            onChange={this.handleChangePassword.bind(this)} />
          <br /><br />
          <TextField
            id='confirm'
            value={this.state.inputConfirm.value}
            error={this.state.inputConfirm.error}
            label={this.state.inputConfirm.label}
            helperText="Confirm password"
            type="password"
            className={classes.textField}
            onChange={this.handleChangeConfirm.bind(this)} />
          <h3 className={classes.labelField}>First Name:</h3>
          <TextField
            id='first'
            value={this.state.inputFirst.value}
            error={this.state.inputFirst.error}
            label={this.state.inputFirst.label}
            helperText="Input first name"
            className={classes.textField}
            onChange={this.handleChangeFirstName.bind(this)} />
          <h3 className={classes.labelField}>Last Name:</h3>
          <TextField
            id='last'
            value={this.state.inputLast.value}
            error={this.state.inputLast.error}
            label={this.state.inputLast.label}
            helperText="Input last name"
            className={classes.textField}
            onChange={this.handleChangeLastName.bind(this)} />
          <h3 className={classes.labelField}>Email:</h3>
          <TextField
            id='email'
            value={this.state.inputEmail.value}
            error={this.state.inputEmail.error}
            label={this.state.inputEmail.label}
            helperText="Input e-mail new user"
            className={classes.textField}
            onChange={this.handleChangeEmail.bind(this)} />
          <br /><br />
          <Button
            id='Button'
            variant='contained'
            color='primary'
            type='submit'
            disabled={this.setEnabledButton()} >
            Register new user
          </Button>
          <br /><br />
        </form>
        <Snackbar id='Snackbar'
          open={this.state.snackbarMessage.open}
          message={this.state.snackbarMessage.message}
          autoHideDuration={4000}
          onClose={this.handleClose.bind(this)}
        />
        <div>
          <Dialog id='Dialog'
            open={this.state.dialogMessage.open}
            onClose={this.handleCloseDialog.bind(this)}
          >
            <DialogTitle id='DialogTitle'>
              {"Registration was successful"}
            </DialogTitle>
            <DialogContent id='DialogContent'>
              <DialogContentText id='DialogContentText'>
                Please go to the link in your letter to confirm the registration
              </DialogContentText>
            </DialogContent>
            <DialogActions id='DialogActions'>
              <Button id='OK'
                onClick={this.handleCloseDialog.bind(this)}
                color="primary"
                autoFocus >
                OK
              </Button>
            </DialogActions>
          </Dialog>
        </div>
      </Paper>
    );
  }
}

export default withStyles(styles)(withRouter(Register));
