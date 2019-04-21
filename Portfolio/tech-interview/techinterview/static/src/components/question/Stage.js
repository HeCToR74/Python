import React from 'react';
import {withRouter} from 'react-router-dom';
import {style} from 'src/layout';
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


const getURL = '/api/questions/sections';
const postURL = '/api/questions/stages';

/**
 * Creates a form to create Stage
 */
export class Stage extends React.Component {
  /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
  constructor(props) {
    super(props);

    this.state = {
      section: {
        value: '',
        error: false,
        label: ' ',
      },
      field: {
        value: '',
        error: false,
        label: ' ',
      },
      sectionField: [],
      valueStage: '',
      snackbar: {
        open: false,
        message: '',
      },
      submitButton: {
        disabled: true,
      },
    };

    // this.style = {
    //   fontFamily: 'Roboto',
    //   height: 'auto',
    //   width: '60%',
    //   margin: 'auto',
    //   marginLeft: '20%',
    //   minWidth: 300,
    //   position: 'relative',
    //   textAlign: 'center',
    //   display: 'inline-block',
    //
    //   nameDiv: {
    //     display: 'block',
    //     margin: 'auto',
    //     paddingBottom: '2em',
    //   },
    //   formControl: {
    //     minWidth: '35%',
    //   },
    //   textField: {
    //     minWidth: '35%'
    //   },
    // };
  }

  /**
   * Change handler for field
   * @param {event} event - Send event from object
   * @param {value} value - Send event from object
   */
  handleChange(event, value) {
    this.setState({section: {value: value.props.value}});
  }

  /**
   * Change handler for valueStage
   * @param {event} event - Send event from object
   */
  handleChangeStage(event) {
    if (event.target.value === '') {
      this.setState({
        field: {
          error: true,
          label: 'Stage can\'t be empty',
        },
        valueStage: '',
      });
      this.setState({submitButton: {disabled: true}});
    } else {
      this.setState({
        valueStage: event.target.value,
        field: {
          error: false,
          label: ' ',
        },
      });
      this.setState({submitButton: {disabled: false}});
    }
  }

  /**
   * Submit handler to send data to API and show message
   * @param {event} event - Send event from object
   */
  handleSubmit(event) {
    event.preventDefault();    
    const serverport = {
      name: this.state.valueStage,
      section: this.state.section.value,
    };
    axios.post(postURL, serverport)
        .then((res) => {
          console.log(res.data);
          this.setState({
            snackbar: {
              message: 'Stage was created',
              open: true,
            },
          }, () => this.props.history.push('/stage'));
        })
        .catch((error) => {
          this.setState({
            snackbar: {
              message: 'Stage isn\'t created',
              open: true,
            },
          });
          console.log(error);
        });
  }

  /**
   * Parsing data for SelectField
   * @return {*} - return parsing sections
   */
  tab() {
    return this.state.sectionField.map(function(object) {
      return <MenuItem key={object.id} value={object.id}>{object.name}</MenuItem>
    });
  }

  /**
   * Data loader before rendering a page
   */
  componentWillMount() {
    axios.get(getURL)
        .then((response) =>{
          this.setState({sectionField: response.data});
          console.log(this.state.sectionField);
        })
        .catch(function(error) {
          console.log(error);
        });
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({snackbar: false });
  } 

  /**
   * Rendering a page
   * @return {*} - return stage component form
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
            <h1>Stage</h1>
              <FormControl id='FormControl' className={classes.textField} >
                <Select 
                  id='section'
                  value={this.state.section.value}
                  onChange={this.handleChange.bind(this)} >
                    {this.tab()}
                </Select>
                <FormHelperText>Section</FormHelperText>
              </FormControl>        
              <br/>
              <TextField
                id='name'
                helperText="Stage"
                onChange={this.handleChangeStage.bind(this)}
                className={classes.textField}
                value={this.state.valueStage}
                error={this.state.field.error}
                label={this.state.field.label}/>              
              <br/><br/>
            <Button id='Button'
              variant='contained'
              color='primary'
              type='submit'
              disabled={this.state.submitButton.disabled} >
              Add Stage
            </Button>              
            <br/><br/>
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
  }
}

export default withStyles(styles)(withRouter(Stage));
