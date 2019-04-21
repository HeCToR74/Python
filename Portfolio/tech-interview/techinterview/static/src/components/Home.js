import React from 'react';
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import { styles } from './../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import {withRouter} from "react-router";


const userURL = '/api/user/user/';
const testURL = '/test/';

/**
 * Home page component
 */
export class Home extends React.Component {
  /**
   * Constructor of class
   * @param {*} props - props from parent object
   */
  constructor(props) {
    super(props);

    this.state = {
      user: {
        id: '',
        login: '',
        first: '',
        last: '',
        email: '',
        role: '',
        interviews_recruiter: '',
        interviews_candidate: '',
        interviews_expert: '',
      },
    };
  }

  /**
   * write componentWillMount
   */
  componentWillMount() {
    axios.get(userURL)
      .then((response) => {
        this.setState({
          user: {
            id: response.data.user.id,
            login: response.data.user.login,
            first: response.data.user.first,
            last: response.data.user.last,
            email: response.data.user.email,
            role: response.data.user.role,
            interviews_recruiter: response.data.user.interviews_recruiter,
            interviews_candidate: response.data.user.interviews_candidate,
            interviews_expert: response.data.user.interviews_expert,
          }
        });
      })
      .catch((error) => console.log(error));
  };

  /**
   * Handler for submit button onClick
   * @param {*} event - current event
   */
  handleClick(event) {
    event.preventDefault();
    this.props.history.push(testURL + this.state.user.interviews_candidate);
  };

  /**
   * Render HTML form
   * @return {*} - Render form to page
   */
  render() {
    const { classes } = this.props;
    return (
      this.state.user.role == 'recruiter' ?
        <React.Fragment>
          <div>
            <Paper
              className={classes.root}
              elevation={20}
            >
              <br />
              Hello, <b>{this.state.user.first} {this.state.user.last}</b>!
            <br /><br />
              Congratulations on techpoll resource
            <br /><br />
              You have <b>{this.state.user.interviews_recruiter}</b> tests
            with the status of the <b>scheduled</b>
              <br /><br />
            </Paper>
          </div>
        </React.Fragment> :
        this.state.user.role == 'candidate' ?
          <React.Fragment>
            <div>
              <Paper
                className={classes.root}
                elevation={20}
              >
                <br />
                Hello, <b>{this.state.user.first} {this.state.user.last}</b>!
              <br /><br />
                Congratulations on techpoll resource
              <br /><br />
                Нou have been given access to pass the testing
              <br /><br />
                <Button variant="contained"
                  color='primary'
                  onClick={this.handleClick.bind(this)}>
                  Start testing
              </Button>
                <br /><br />
              </Paper>
            </div>
          </React.Fragment> :
          <React.Fragment>
            <div>
              <Paper
                className={classes.root}
                elevation={20}
              >
                <br />
                Hello, <b>{this.state.user.first} {this.state.user.last}</b>!
              <br /><br />
                Congratulations on techpoll resource
              <br /><br />
              </Paper>
            </div>
          </React.Fragment>
    );
  }
}

export default withStyles(styles)(withRouter(Home));
