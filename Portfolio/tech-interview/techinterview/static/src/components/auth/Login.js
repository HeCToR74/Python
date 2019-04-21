import React from 'react';
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withRouter } from "react-router-dom";
import GoogleLogin from 'react-google-login';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';


/**
 * Login form component
 */
class Login extends React.Component {
  /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
  constructor(props) {
    super(props);

    this.state = {
      field: {
        value: '',
        error: '',
      },
      textFieldLogin: {
        value: '',
        error: '!',
      },
      textFieldPassword: {
        value: '',
        error: '!',
      },
      snackbar: {
        open: false,
        message: '',
      },
      submitButton: {
        disabled: true,
      },
    };
  }

  /**
   * Change handler for inputLogin
   */
  handleChangeLogin(event) {
    if (event.target.value !== '') {
      this.setState({ textFieldLogin: { value: event.target.value } });
    } else {
      this.setState({ textFieldLogin: { error: 'Login can\'t be empty' } });
    }
  };

  /**
   * Change handler for inputPass
   */
  handleChangePassword(event) {
    if (event.target.value !== '') {
      this.setState(
        { textFieldPassword: { value: event.target.value },
          snackbar: {
            message: '',
            open: false,
          },
        });
    } else {
      this.setState({ textFieldPassword: {
          error: 'Password can\'t be empty' },
        snackbar: {
          message: '',
          open: false,
        },
      });
    }
  };

  /**
   * Handle submit
   * @param {e} e - e is for submit
   */
  handleSubmit(e) {
    e.preventDefault();
    const user = {
      username: this.state.textFieldLogin.value,
      password: this.state.textFieldPassword.value,
    };
    axios.post('/api/user/login/', user)
      .then((res) => {
        this.props.history.push('/home/');
      })
      .catch((error) => {
        this.setState({
          snackbar: {
            message: 'Wrong login',
            open: true,
          },
        });
      });

  };

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({snackbar: { open: false } });
  }

  /**
   * Render HTML form with handlers
   * @return {React} - Render form to page
   */
  render() {
    const { classes } = this.props;
    return (
      <div>
        <Paper className={classes.root} elevation={20}>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <h2>Username</h2>
            <TextField 
              placeholder='username' 
              onChange={this.handleChangeLogin.bind(this)}
              className={classes.textField} />
            <br/>
            <h2>Password</h2>
            <TextField 
              placeholder='password' 
              name="password"                       
              type="password"
              onChange={this.handleChangePassword.bind(this)}
              className={classes.textField} />
            <br/><br/>
            <Button variant='contained'
                    color='primary'
                    type="submit"
                    overlayStyle={{height:'auto'}}
                    style={{height: '42px', width: '163px'}}>
              Login
            </Button>
            <br/><br/>
            <GoogleLogin
              clientId="866849218580-4e9jhfoliq95sf95hf5rd5cvgf1ohocf.apps.googleusercontent.com"
              buttonText="Login via Google"
              onSuccess={(googleUser) => {
                const id_token = googleUser.getAuthResponse().id_token;
                const config = {
                  headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                  }
                };
                axios.post('/api/user/google/', `idtoken=${id_token}`, config)
                  .then(response => this.props.history.push('/home/'));
              }}
              onFailure={() => this.setState({
                  snackbar: {
                    message: 'Wrong login',
                    open: true,
                  },
                },
                () => setTimeout(() =>
                  this.setState({snackbar: {open:false}}), 4000))}
            />
            <br/><br/>
          </form>
          <Snackbar
            open={this.state.snackbar.open}
            message={this.state.snackbar.message}
            autoHideDuration={4000}
            onClose={this.handleClose.bind(this)}
          />
        </Paper>
      </div>
    );
  }
}

export default withStyles(styles)(withRouter(Login));
