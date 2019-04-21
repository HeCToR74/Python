import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import { withRouter } from 'react-router-dom';
import Input from '@material-ui/core/Input';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import FilledInput from '@material-ui/core/FilledInput';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import axios from 'axios';

export class DropDownRes extends React.Component {
  constructor(props) {
    super(props);
    const {defaultValue} = this.props;
    this.state = {
      value: defaultValue,
      name: '',
      labelWidth: 0,
    };

    this.handleOpen = this.handleOpen.bind(this);
    this.handleChange = this.handleChange.bind(this);
  };

  handleChange(event) {
    this.setState({value: event.target.value });
  };
  handleOpen() {
    this.setState({ open: true });
  };

  render() {
    const {value} = this.state;
    const {name, values} = this.props;
    const { classes } = this.props;

    return (
      <React.Fragment>
        <form className={classes} autoComplete="off">
          <FormControl className={classes.formControl}>
            <Select
              value={this.props.selectValue}
              onChange={this.props.handleChange}
              displayEmpty
              name={name}
              className={classes.selectEmpty}
            >
              {
                values && values.map((item, index) => (
                  <MenuItem value={item.value} key={index}>
                    {item.value}
                  </MenuItem>
                ))
              }
            </Select>

          </FormControl>
        </form>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(DropDownRes));
