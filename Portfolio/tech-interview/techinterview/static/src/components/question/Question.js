import React from 'react';
import {withRouter} from 'react-router-dom';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import Paper from '@material-ui/core/Paper';
import Select from '@material-ui/core/Select';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import MenuItem from '@material-ui/core/MenuItem';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';

/**
 * Creates a form to create Question
 */
class Question extends React.Component {
   /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
  constructor(props) {
    super(props);

    this.state = {
      inputName: {
        value: '',
        error: false,
        label: ' ',
      },

      inputHint: {
        value: '',
        error: false,
        label: ' ',
      },

      inputStage: {
        value: '',
        json: {},
      },

      stageField: [],

      snackbar: {
        open: false,
        message: '',
      },

      submitButton: {
        disabled: true,
        label: 'Add Question',
      },

      pushMethod: 'POST',
      pushURL: '/api/questions/questions/',
      hideDelay: 2000,
    };
  }

  /**
   * Change handler for input name
   * @param {event} event - Send event from object
   */
  handleChangeName(event) {
    if (event.target.value === '') {
      this.setState({
        inputName: {
          error: true,
          label: 'Name can\'t be empty',
        },
        submitButton: {disabled: true},
        snackbar: {open: false},
      });
    } else {
      this.setState({
        inputName: {
          value: event.target.value,
          error: false,
          label: ' ',
        },
        submitButton: {
          disabled: true,
          label: this.state.submitButton.label,
        },
        snackbar: {open: false},
      });
    }
  }

   /**
   * Change handler for input hint
   * @param {event} event - Send event from object
   */
  handleChangeHint(event) {
    if (event.target.value === '') {
      this.setState({
        inputHint: {
          error: true,
          label: 'Name can\'t be empty',
        },
        snackbar: {open: false},
      });
    } else {
      this.setState({
        inputHint: {
          value: event.target.value,
          error: false,
          label: ' ',
        },
        submitButton: {
          disabled: true,
          label: this.state.submitButton.label,
        },
        snackbar: {open: false},
      });
    }
  }

   /**
   * Change handler for input stage
   * @param {event} event - Send event from object
   */
  handleChangeStage(event, value, dir) {
    axios.get('/api/questions/stages/' + value.props.value + '/')
        .then((res) => {
          this.setState({
            inputStage: {
              value: value.props.value,
              json: res.data,
            }
        }) });
    this.setState({
      submitButton: {
        disabled: false,
        label: this.state.submitButton.label,
      },
      snackbar: {open: false},
    });
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
        axios.get('/api/questions/stages/' + this.state.inputStage.value + '/')
          .then((response) => {
            this.setState({inputStage: {
              json: response.data,
            } });
          });
     if (this.state.inputName.value != '' && this.state.inputHint.value != ''){
        this.setState({
          snackbar: {
            message: 'Question was created',
            open: true,
          },
        });
        await axios({
          method: this.state.pushMethod,
          url: this.state.pushURL,
          data: {
            name: this.state.inputName.value,
            hint: this.state.inputHint.value,
            stage: this.state.inputStage.json,
          },
        })
        this.setState({
            submitButton: {
                disabled: true,
                label: this.state.submitButton.label,
            },
        });
        await this.setState({
            snackbar: {
                message: 'Question was created',
                open: true,
            },
        });
        setTimeout(() => this.props.history.push('/question'), this.state.hideDelay);
     }
     else {
         this.setState({
            snackbar: {
                message: 'Name or Hint can\'t be empty',
                open: true,
             }});
     }
  }

   /**
   * Data loader if page loads with id in URL
   */
  componentWillMount() {
    axios.get('/api/questions/stages/')
        .then((response) =>{
          this.setState({stageField: response.data});
        })
        .catch(function(error) {
          console.log(error);
        });
    if (this.props.match.params.id) {
      axios('/api/questions/questions/' + this.props.match.params.id)
          .then(function(response) {
            return response.data;
          })
          .then((json) => {
            this.setState({
              inputName: {value: json.name},
              inputHint: {value: json.hint},
              inputStage: {value: json.stage.id},
              pushMethod: 'PUT',
              pushURL: '/api/questions/questions/' + this.props.match.params.id,
              submitButton: {label: 'Edit Section'},
            });
      axios.get('/api/questions/stages/' + this.state.inputStage.value + '/')
        .then((response) => {
          this.setState({inputStage: {
            value: response.data.id,
            json: response.data,
          } });
        });
      });
    }
  }

  tab() {
    return this.state.stageField.map(function(object) {
      return <MenuItem key={object.id} value={object.id}>{object.name}</MenuItem>;
    });
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
          <form onSubmit={this.handleSubmit.bind(this)} >
            <h1>Question:</h1>
            <div className={classes.nameDiv}>
              <TextField              
                id='name'
                helperText="Question"
                onChange={this.handleChangeName.bind(this)}
                value={this.state.inputName.value}
                error={this.state.inputName.error}
                label={this.state.inputName.label}
                className={classes.textField} />
            </div>
            <h1>Hint:</h1>
            <div className={classes.nameDiv}>
              <TextField
                id='hint'
                helperText="Hint"
                className={classes.textField}
                onChange={this.handleChangeHint.bind(this)}
                value={this.state.inputHint.value}
                error={this.state.inputHint.error}
                label={this.state.inputHint.label} />
            </div>
            <div className={classes.nameDiv}>
              <h1>Stage:</h1>
              <FormControl id='FormControl' className={classes.textField} >
                <Select
                  id='Stage'
                  value={this.state.inputStage.value}
                  onChange={this.handleChangeStage.bind(this)} >
                    {this.tab()}
                </Select>
                <FormHelperText>Stage</FormHelperText>
              </FormControl> 
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
            autoHideDuration={2000}
            onClose={this.handleClose.bind(this)}
          />
        </Paper>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(Question));
