import React from 'react';
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import {withRouter} from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import { expRegPass } from 'src/constants.js';


const pushURL = '/api/user/password_reset/confirm/';

export class PasswordResetConfirm extends React.Component {
  /**
   * Constructor of class
   */
  constructor(props) {
    super(props);

    this.state = {
      inputPass: {
        value: '',
        error: false,
        label: ' ',
      },
      inputConfirm: {
        value: '',
        error: false,
        label: ' ',
      },
      snackbar: {
        message: 'Password change',
        open: true,
      },
    };
  }

  /**
   * Change handler for textfield
   */
  handleChangePassword(event) {
    if (event.target.value === '') {
      this.setState({ inputPass: {
        value: '',
        error: true,
        label: 'Password can\'t be empty',
      } });
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
            label: 'Password is not valid. Ex: "qwe123Q!"',
          },
        });
      }
      expRegPass.test(event.target.value);
    }
    if (this.state.inputConfirm.value !== '') {
      this.setState({
        inputConfirm: {
          value: this.state.inputConfirm.value,
          error: event.target.value !== this.state.inputConfirm.value ? true : false,
          label: event.target.value !== this.state.inputConfirm.value ? 'Passwords do not match' : ' ',
        },
      });
    }
  };


  /**
   * Change handler for inputConfirm
   */
  handleChangeConfirm(event){
    this.setState({
      inputConfirm: {
        value: event.target.value,
        error: event.target.value !== this.state.inputPass.value ? true: false,
        label: event.target.value !== this.state.inputPass.value ? 'Passwords do not match' : ' ',
      },
    });
  };


  /**
   * Submit handler to send data to API and show message
   */
  handleSubmit(event) {
    event.preventDefault();
    if (this.state.inputPass.value !== '') {
      this.setState({
        snackbar: {
          message: 'Password change',
          open: true,
        },
      });

      const serverport = {
        password: this.state.inputConfirm.value,
        token: this.props.match.params.token,
      };
      console.log(this.props.match.params.token);
      console.log(serverport);

      axios.post(pushURL, serverport)
        .then((res) => {
          this.props.history.push('/login/');
        })
        .catch((error) => {});
      this.state = {
        inputPass: {
          value: '',
          error: false,
          label: ' ',
        },
        inputConfirm: {
          value: '',
          error: false,
          label: ' ',
        },
      };
    };
  };

  /**
   * Render HTML form with handlers
   */
  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <Paper id='Paper' className={classes.root} elevation={20}>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <h3 className={classes.labelField}>Change password</h3>
            <TextField
              id='password1'
              helperText="Input new password"
              onChange={this.handleChangePassword.bind(this)}
              value={this.state.inputPass.value}
              error={this.state.inputPass.error}
              label={this.state.inputPass.label}
              className={classes.textField}
              type = "password"/>
            <br />
            <TextField
              id='password2'
              helperText="Repeat password"
              onChange={this.handleChangeConfirm.bind(this)}
              value={this.state.inputConfirm.value}
              error={this.state.inputConfirm.error}
              label={this.state.inputConfirm.label}
              className={classes.textField}
              type = "password"/>
            <br /><br />
            <Button
              id='Button'
              variant='contained'
              type='submit'
              color='primary' >
              Change password
            </Button>
            <br /><br />
          </form>
        </Paper>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(PasswordResetConfirm));
