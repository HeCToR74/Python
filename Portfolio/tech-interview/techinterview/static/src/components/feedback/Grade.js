import React from 'react';
import axios from 'axios';
import {NavLink} from 'react-router-dom';
import {withRouter} from 'react-router-dom';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import Snackbar from "@material-ui/core/Snackbar";
import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";


/**
 * Table for show up all grades
 */
export class Grade extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      inputName: {
        value: '',
        error: false,
        label: ' ',
      },
      inputWeight: {
        value: '',
        error: false,
        label: ' ',
      },
      snackbar: {
        open: false,
        message: '',
      },
      submitButton: {
        disabled: true,
        label: 'Add Grade',
      },
      pushMethod: 'POST',
      pushURL: '/api/feedback/grades/',
      hideDelay: 1000,
    };
  }

  /**
   * Change handler for inputName
   * @param {event} event - Send event from object
   */
  handleChangeName(event) {
    if (event.target.value === '') {
      this.setState({
        inputName: {
          error: true,
          label: 'Name can\'t be empty',
        },
        submitButton: {label: this.state.submitButton.label, disabled: true},
        snackbar: {open: false},
      });
    } else {
      this.setState({
        inputName: {
          value: event.target.value,
          error: false,
          label: ' ',
        },
        submitButton: {label: this.state.submitButton.label, disabled: false},
        snackbar: {open: false},
      });
    }
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({ snackbar: false });
  }

  /**
   * Change handler for inputWeight
   * @param {event} event - Send event from object
   */
  handleChangeWeight(event) {
    if (event.target.value === '') {
      this.setState({
        inputWeight: {
          error: true,
          label: 'Weight can\'t be empty',
        },
        submitButton: {label: this.state.submitButton.label, disabled: true},
        snackbar: {open: false},
      });
    } else {
      this.setState({
        inputWeight: {
          value: event.target.value,
          error: false,
          label: ' ',
        },
        submitButton: {label: this.state.submitButton.label, disabled: false},
        snackbar: {open: false},
      });
    }
  }

  /**
   * Submit handler to send data to API and show message
   * @param {event} event - Send event from object
   */
  async handleSubmit(event) {
    try {
        event.preventDefault();
        await axios({
          method: this.state.pushMethod,
          url: this.state.pushURL,
          data: {
            name: this.state.inputName.value,
            weight: this.state.inputWeight.value,
          },
        });
        await this.setState({
          snackbar: {
            message: 'Grade was created',
            open: true,
          },
        });

        setTimeout(() => this.props.history.push(`/grade`), this.state.hideDelay);
    } catch (error) {
      this.setState({
            snackbar: {
                message: "Can't add the grade",
                open: true,
            },
        });
        console.log('here is error', error);
    }
  }

   /**
   * Data loader if page loads with id in URL
   */
  componentWillMount() {
    if (this.props.match.params.id) {
      axios('/api/feedback/grades/' + this.props.match.params.id)
          .then(function(response) {
            return response.data;
          }).then((json) => {
            this.setState({
              inputName: {value: json.name},
              inputWeight: {value: json.weight},
              pushMethod: 'PUT',
              pushURL: '/api/feedback/grades/' + this.props.match.params.id,
              submitButton: {label: 'Edit Grade'},
            });
          });
    }
  }

  /**
   * Render filled table
   * @return {*} - return component
   */
  render() {
    const { classes } = this.props;
    return (
        <React.Fragment>
          <Paper className={classes.root} elevation={20}>
            <form onSubmit={this.handleSubmit.bind(this)}>
               <h1>Grade:</h1>
                <TextField
                  id='name'
                  helperText="input name"
                  onChange={this.handleChangeName.bind(this)}
                  className={classes.textField}
                  value={this.state.inputName.value}
                  error={this.state.inputName.error}
                  label={this.state.inputName.label} /> 
                <h1>Weight:</h1>
                    <TextField
                        id='weight'
                        helperText="input weight"
                        className={classes.textField}
                        onChange={this.handleChangeWeight.bind(this)}
                        value={this.state.inputWeight.value}
                        error={this.state.inputWeight.error}
                        label={this.state.inputWeight.label} />
                <br/><br/>
                <Button
                  id="Button"
                  variant="contained"
                  color="primary"
                  type="submit"
                  disabled={this.state.submitButton.disabled}
                >
                  {this.state.submitButton.label}
                </Button>
                <br/>
                <br/>
            </form>
            <Snackbar
              open={this.state.snackbar.open}
              message={this.state.snackbar.message}
              autoHideDuration={this.state.hideDelay}
              onClose={this.handleClose.bind(this)}
             />
        </Paper>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(Grade));
