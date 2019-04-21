import React, {Component} from 'react';
import Select from '@material-ui/core/Select';
import Input from '@material-ui/core/Input';
import MenuItem from '@material-ui/core/MenuItem';
import axios from 'axios';
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";

/**
 * Implement dropdown with grades
 */
export default class SelfEstimateDropDown extends Component {
  /**
   * Set default value and get all grade names
   * @param {*} props - parent data
   */
  constructor(props) {
    super(props);
    this.state = {
      value: 1,
      grades: [],
    };

    this.onChange = this.onChange.bind(this);
  }

  /**
   * Fetch data from API
   */
  componentWillMount() {
    axios('/api/feedback/grades/')
        .then((response) => this.setState({grades: response.data}));
    this.setState({value: this.props.selected});
  }

  /**
   * Change selected value and send it to parent object
   * @param {event} event  - html object
   * @param {index} index - index in array
   * @param {value} value - id in database
   */
  onChange(event) {
    this.setState({value: event.target.value});
    this.props.onChange(event.target.value);
  }

  /**
   * Render dropdown
   * @return {*} -Filled dropdown
   */
  render() {
    return (
      <div>
        <FormControl>
        <InputLabel htmlFor="grade">Grade</InputLabel>
        <Select
          value={this.state.value}
          onChange={this.onChange}
          style={{minWidth: 120}}
          input={<Input name="age" id="grade" />}
        >
          {this.state.grades.map((value, index) =>
            (<MenuItem value={value.id} key={index}>{value.name}</MenuItem>)
          )
          }
        </Select>
        </FormControl>
      </div>
    );
  }
}
