import React from 'react';
import axios from 'axios';
import { styles } from './../../styles/styles';
import { withRouter } from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import Paper from '@material-ui/core/Paper';
import Select from '@material-ui/core/Select';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import MenuItem from '@material-ui/core/MenuItem';
import ListItemText from '@material-ui/core/ListItemText';
import Checkbox from '@material-ui/core/Checkbox';
import Input from '@material-ui/core/Input';


export class Department extends React.Component {
  /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
  constructor(props) {
    super(props);

    this.state = {

      questions: [],
      values: [],
      ids: [],
      textField: {
        value: '',
        error: false,
        label: ' '
      },
      snackbar: {
        open: false,
        message: '',
      },
      submitButton: {
        label: 'Add Department',
        disabled: true,
      },
      pushMethod: 'POST',
      pushURL: '/api/departments/',
      questionsURL: '/api/questions/questions/'
    };
  }

  handleChange(event) {
    if ((event.target.value !== '') && (this.state.values.length !== 0)) {
      this.setState({
        submitButton: {
          label: this.state.submitButton.label,
          disabled: false
        }
      })
    }
    else {
      this.setState({
        submitButton: {
          label: this.state.submitButton.label,
          disabled: true
        }
      })
    }
    if ((event.target.value === '')) {
      this.setState({
        textField: {           
          value: event.target.value,
          error: true,
          label: 'Name can\'t be empty',
        }
      });
    }
    else {
      this.setState({
        textField: { 
          value: event.target.value,
          error: false,
          label: ' ',
        },
        snackbar: {
          message: '',
          open: false,
        },
      });
    }
  }

  handleSubmit(event) {
    event.preventDefault();
    let department = {};
    if (this.props.match.params.id) {
      department = {
        id: this.props.match.params.id,
        name: this.state.textField.value,
        questions: this.state.ids,
      };
    } else {
      department = {
        name: this.state.textField.value,
        questions: this.state.ids,
      };
    }
    this.setState({
      snackbar: {
        message: 'Department was created',
        open: true,
      },
      textField: {
        value: '',
        error: false,
        label: ' ',
      },
      values: [],
      ids: [],
    });
    axios({
      method: this.state.pushMethod,
      url: this.state.pushURL,
      data: department,
    })
      .then((res) => this.props.history.push('/department/'))
      .catch(function (error) {
        console.log(error);
      });
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({ snackbar: false });
  }

  componentDidMount() {
    console.log(this.props);
    axios.get(this.state.questionsURL)
      .then((response) => {
        this.setState({ questions: response.data });
      })
      .catch(function (error) {
        console.log(error);
      });

    if (this.props.match.params.id) {
      axios(this.state.pushURL + this.props.match.params.id + '?raw=true')
        .then(function (response) {
          return response.data;
        }).then((json) => {
          this.setState({
            textField: { value: json.name },
            ids: json.questions.map((value) => {
              return value.id;
            }),
            values: json.questions.map((value) => {
              return value.name;
            }),
            pushMethod: 'PUT',
            pushURL: this.state.pushURL + this.props.match.params.id,
            submitButton: { label: 'Edit Department', disabled: false },

          });
        });
    }
  }

  handleQuChange(event) {
    const values = event.target.value;    
    const ids = [];
    for (let i in this.state.questions) {
      if (values.indexOf(this.state.questions[i]['name']) != -1) {
        ids.push(this.state.questions[i]['id']);
      }
    }
    if ((this.state.textField.value !== '') && (values.length !== 0)) {
      this.setState({
        submitButton: {
          label: this.state.submitButton.label,
          disabled: false
        }
      })
    }
    else {
      this.setState({
        submitButton: {
          label: this.state.submitButton.label,
          disabled: true
        }
      })
    }
    this.setState({ 
      values: values,
      ids: ids,
    });
  }

  menuItems() {
    return this.state.questions.map((question, i) => (
      <MenuItem key={i} value={question.name} >
        <Checkbox checked={this.state.values.indexOf(question.name) > -1} />
        <ListItemText primary={question.name} />
      </MenuItem>
    ));
  }


  render() {
    const { classes } = this.props;
    const { values } = this.state;
    return (
      <React.Fragment>
        <Paper id='Paper' style={styles} elevation={20}>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <h1>Department:</h1>
              <TextField
                id='department'
                helperText="Name"
                onChange={this.handleChange.bind(this)}
                value={this.state.textField.value}
                error={this.state.textField.error}
                label={this.state.textField.label}
                style={styles.textField} />
              <br />
              <FormControl id='FormControl' style={styles.formControl}>
                <Select id='questions'
                  multiple
                  value={this.state.values}
                  onChange={this.handleQuChange.bind(this)}
                  input={<Input/>}
                  renderValue={selected => selected.join(', ')} 
                >               
                  {this.menuItems()}
                </Select>
                <FormHelperText>Select questions</FormHelperText>
              </FormControl>
            <br/><br/>
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
            autoHideDuration={4000}
            onClose={this.handleClose.bind(this)}
          />
        </Paper>
      </React.Fragment>
    );
  }
}

export default (withRouter(Department));
