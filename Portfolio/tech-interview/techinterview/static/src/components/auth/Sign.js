import React from 'react';
import PropTypes from 'prop-types';
import { withRouter, Redirect, Link, NavLink } from 'react-router-dom';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import AppBar from '@material-ui/core/AppBar';

/**
 * Sign Up form component
 */
export class Sign extends React.Component {
  /**
   * Constructor of class
   */
  constructor(props) {
    super(props);

    this.state = {
      value: this.props.history.location.pathname.slice(1,-1),
    };
  };

  /**
   * Change handler for inputLogin
   * @param {*} event - current event
   * @param {*} val - current value
   */
  handleChange(event, val) {
    this.setState({ value: val });
    this.props.history.push('/' + val + '/');
  };

  /**
   * Render HTML form
   * @return {*} - Render form to page
   */
  render() {
    return (
      <React.Fragment>
        <AppBar position="fixed" >
          <Tabs
            id='Tabs'
            value={this.state.value}
            variant="fullWidth"
            onChange={this.handleChange.bind(this)}
          >
            <Tab id='Tab' label='Register' value='register' />
            <Tab id='Tab' label='Login' value='login' />
            <Tab id='Tab' label='Forget password' value='password_reset' />
          </Tabs>
        </AppBar>
        <br/><br/><br/>
      </React.Fragment>
    );
  }
}

export default withRouter(Sign);
