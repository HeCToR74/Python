import React from 'react';
import axios from 'axios';
import {withRouter} from 'react-router-dom';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Snackbar from '@material-ui/core/Snackbar';
import { expRegEmail } from 'src/constants.js';


const pushMethod = 'POST';
const pushURL= '/api/user/password_reset/';

/**
 * Creates a form to create new user
 */
export class PasswordReset extends React.Component {
  // state = { redirectToReferrer: false };
  /**
   * Constructor of class
   */
  constructor(props) {
    super(props);

    this.state = {
      inputEmail: {
        value: '',
        error: false,
        label: ' '
      },
      snackbar: {
        message: '',
        open: false,
      },
    };
  }

  /**
   * Change handler for textfield email
   * @param{event} event
   */
  handleChangeEmail(event) {
    if (event.target.value !== '') {
      this.setState({inputEmail: {value: event.target.value}});
      // console.log(this.state.inputEmail.value);
    }
    if (!expRegEmail.test(event.target.value)) {
      this.setState({inputEmail: {
        value: event.target.value,
        error: true,
        label: 'Email is not valid'
      }});
    };
    expRegEmail.test(event.target.value)
  };

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({snackbar: { open: false } });
  }

  /**
   * Submit handler to send data to API and show message
   * @param{event} event
   */
  handleSubmit(event) {
    event.preventDefault();
    this.setState({
      snackbar: {
        message: 'Password change',
        open: true,
      },
    });

    const date = {
      email: this.state.inputEmail.value,
    };

    console.log(date);
    axios.post(pushURL, date)
      .then((res) => {
        this.props.history.push('/login/');
      })
      .catch((error) => {
        this.setState({
          snackbar: {
            message: 'Email not found',
            open: true,
          },
        });
      });
    this.state = {
      inputEmail: {
        value: '',
        error: '',
      },
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
            <h3 className={classes.labelField}>Email</h3>
            <TextField
              id='email'
              value={this.state.inputEmail.value}
              error={this.state.inputEmail.error}
              label={this.state.inputEmail.label}
              helperText="Input e-mail for forgot password"
              onChange={this.handleChangeEmail.bind(this)}
              className={classes.textField}
            />
            <br/><br/>
            <Button
              id='Button'
              variant='contained'
              type='submit'
              color='primary' >
              Forgot Password
            </Button>
            <br /><br />
          </form>
          <Snackbar
            open={this.state.snackbar.open}
            message={this.state.snackbar.message}
            autoHideDuration={4000}
            onClose={this.handleClose.bind(this)}
          />
        </Paper>
      </React.Fragment>
    );
  };
}

export default withStyles(styles)(withRouter(PasswordReset));
