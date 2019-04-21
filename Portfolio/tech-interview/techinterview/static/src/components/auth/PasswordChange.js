import React from 'react';
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withRouter } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import Snackbar from "src/components/auth/PasswordReset";
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { expRegPass } from 'src/constants.js';


const changePassUrl = '/api/user/password/change/'

export class PasswordChange extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      open: false,
      inputPass: {
        value: null,
        error: false,
        label: ' ',
      },
      inputConfirm: {
        value: null,
        error: false,
        label: ' ',
      },
      inputOldPass: {
        value: null,
        error: false,
        label: ' ',
      },
    };
  };

  handleOpen() {
    this.setState({ open: true });
  };

  handleClose() {
    this.setState({ open: false });
  };

  /**
   * Change handler for textfield
   */
  handlePasswordChange(event) {
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
  handleOldPassword(event) {
    this.setState({
      inputOldPass: {
        value: event.target.value,
        error: false,
        label: ' ',
      },
    });
  };
  handleSubmit(event) {
    event.preventDefault();

    const serverport = {
      old_password: this.state.inputOldPass.value,
      new_password1: this.state.inputPass.value,
      new_password2: this.state.inputConfirm.value,
    };

    axios.post(changePassUrl, serverport)
      .then((res) => {
        this.setState({
          inputPass: { value: '', error: '', label: ' ' },
          inputConfirm: { value: '', error: '', label: ' ' },
          inputOldPass: { value: '', error: '', label: ' ' },
          open: false,
        });
      })
      .catch((error) => {
        this.setState({
          inputOldPass: {
            value: '',
            error: true,
            label: 'invalid password',
          },
        })
      });
  };

  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <Button
          id='changePassword'
          variant='contained'
          className={classes.button}
          onClick={this.handleOpen.bind(this)}
          color='primary' >
          Change password
        </Button>
        <Dialog
          open={this.state.open}
          onClose={this.handleClose.bind(this)} >
          <DialogTitle id='DialogTitle'>
            {"Password change"}
          </DialogTitle>
          <DialogContent>
            <DialogContentText>
              <TextField
                id='old_password'
                helperText="Input old password"
                type="password"
                onChange={this.handleOldPassword.bind(this)}
                value={this.state.inputOldPass.value}
                error={this.state.inputOldPass.error}
                label={this.state.inputOldPass.label}
                className={classes.textField}
              />
              <br/>
              <TextField
                id='new_password1'
                helperText="Input new password"
                type="password"
                onChange={this.handlePasswordChange.bind(this)}
                value={this.state.inputPass.value}
                error={this.state.inputPass.error}
                label={this.state.inputPass.label}
                className={classes.textField}
              />
              <br/>
              <TextField
                id='new_password2'
                helperText="Repeat new password"
                type="password"
                onChange={this.handleChangeConfirm.bind(this)}
                value={this.state.inputConfirm.value}
                error={this.state.inputConfirm.error}
                label={this.state.inputConfirm.label}
                className={classes.textField}
              />
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button
              onClick={this.handleClose.bind(this)}
              color="primary" >
              Cancel
            </Button>
            <Button
              onClick={this.handleSubmit.bind(this)}
              color="primary"
              autoFocus >
              Submit
            </Button>
          </DialogActions>
        </Dialog>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(PasswordChange));
