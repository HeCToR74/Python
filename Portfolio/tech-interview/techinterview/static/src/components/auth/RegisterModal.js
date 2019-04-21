import React from "react";
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import { withRouter } from 'react-router-dom';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { expRegEmail } from 'src/constants.js';


const registerAPI = '/api/user/registration/';

export class RegisterModal extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      firstName: { error: false, value: '', label: ' ' },
      lastName: { error: false, value: '', label: ' ' },
      email: { error: false, value: '', label: ' ' },
    };
  }

  handleChangeFirstName(event) {
    if (event.target.value === '') {
      this.setState({
        firstName: {
          error: true,
          label: 'Last name can\'t be empty',
        }
      });
    } else {
      this.setState({
        firstName: {
          value: event.target.value,
          error: false,
          label: ' ',
        }
      });
    }
  };

  handleChangeLastName(event) {
    if (event.target.value === '') {
      this.setState({
        lastName: {
          error: true,
          label: 'Last name can\'t be empty',
        }
      });
    } else {
      this.setState({
        lastName: {
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
          email: {
            value: event.target.value,
            error: false,
            label: ' ',
          }
        });
      } else {
        this.setState({
          email: {
            value: event.target.value,
            error: true,
            label: 'Email is not valid. Ex: "user@mail.com"',
          },
        });
      }
    } else {
      this.setState({
        email: {
          error: true,
          label: 'Email can\'t be empty'
        }
      });
    }
  };

  handleSubmit(event) {
    const data = {
      first_name: this.state.firstName.value,
      last_name: this.state.lastName.value,
      email: this.state.email.value
    };
    axios
      .post(registerAPI + this.props.role.toLowerCase(), data)
      .then(response => this.props.onSubmit(response.data))
  }

  render() {
    const { classes } = this.props;
    return (
      <Dialog
        open={this.props.open}
        className={classes}
        onClose={this.props.onClose}
      >
        <DialogTitle>
          {this.props.role + " Registration"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText>
            <h3 className={classes}>First Name:</h3>
            <TextField
              id='first_name'
              helperText="Input first name new user"
              onChange={this.handleChangeFirstName.bind(this)}
              className={classes}
              error={this.state.firstName.error}
              label={this.state.firstName.label} />
            <h3 className={classes}>Last Name:</h3>
            <TextField
              id='last_name'
              helperText="Input last name new user"
              onChange={this.handleChangeLastName.bind(this)}
              className={classes}
              error={this.state.lastName.error}
              label={this.state.lastName.label} />
            <h3 className={classes}>Email:</h3>
            <TextField
              id='email'
              helperText="Input e-mail new user"
              onChange={this.handleChangeEmail.bind(this)}
              className={classes}
              error={this.state.email.error}
              label={this.state.email.label} />
            <br />
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button
            onClick={this.props.onClose}
            color="primary" >
            Cancel
          </Button>
          <Button
            onClick={this.handleSubmit.bind(this)}
            color="secondary"
            autoFocus >
            Create
          </Button>
        </DialogActions>
      </Dialog>
    );
  }
}

export default withStyles(styles)(withRouter(RegisterModal));
