import React from 'react';
import {style} from 'src/layout';
import axios from 'axios';
import {withRouter} from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import Paper from '@material-ui/core/Paper';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';


/**
 * Creates a form to create Section
 */
export class Section extends React.Component {
  /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
  constructor(props) {
    super(props);

    this.state = {
      textField: {
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
        label: 'Add Section',
      },
      pushMethod: 'POST',
      pushURL: '/api/questions/sections/',
      hideDelay: 1000,
    };
  }

  /**
   * Data loader if page loads with id in URL
   */
  componentDidMount() {
    if (this.props.match.params.id) {
      axios('/api/questions/sections/' + this.props.match.params.id)
          .then(function(response) {
            return response.data;
          }).then((json) => {
            this.setState({
              textField: {value: json.name},
              pushMethod: 'PUT',
              pushURL: '/api/questions/sections/' + this.props.match.params.id,
              submitButton: {label: 'Edit Section'},
            });
          });
    }
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({snackbar: { open: false } });
  } 

  /**
   * Change handler for textfield
   * @param {event} event - Send event from object
   */
  handleChange(event) {
    if (event.target.value === '') {
      this.setState({
        textField: {
          error: true,
          label: 'Name can\'t be empty',
        },
        submitButton: {label: this.state.submitButton.label, disabled: true},
        snackbar: {open: false},
      });
    } else {
      this.setState({
        textField: {
          value: event.target.value,
          error: false,
          label: ' ',
        },
        submitButton: {label: this.state.submitButton.label,
          disabled: false},
        snackbar: {open: false},
      });
    }
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({snackbar: false });
  }

  /**
   * Submit handler to send data to API and show message
   * @param {event} event - Send event from object
   */
  async handleSubmit(event) {
    event.preventDefault();
    await axios({
      method: this.state.pushMethod,
      url: this.state.pushURL,
      data: {
        name: this.state.textField.value,
      },
    });
    await this.setState({
      snackbar: {
        message: 'Section was created',
        open: true,
      },
    });

    setTimeout(() => this.props.history.push(`/section`), this.state.hideDelay);
  }

  /**
   * Render HTML form with handlers
   * @return {React} - Render form to page
   */
  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <Paper id='Paper'
               className={classes.root}
               elevation={20}
        >
          <form onSubmit={this.handleSubmit.bind(this)}>
            <h1>Section:</h1>
            <div className={classes.nameDiv} id='nameDiv'>
              <TextField
                id='name'
                helperText="Name"
                className={classes.textField}
                onChange={this.handleChange.bind(this)}
                value={this.state.textField.value}
                error={this.state.textField.error}
                label={this.state.textField.label} 
              />
            </div>
            <Button id='Button'
              variant='contained'
              color='primary'
              type='submit'
              disabled={this.state.submitButton.disabled} >
              {this.state.submitButton.label}
            </Button>
            <br/><br/>
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

export default withStyles(styles)(withRouter(Section));
