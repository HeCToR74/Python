import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import cyan from '@material-ui/core/colors/cyan';
import deepPurple from '@material-ui/core/colors/deepPurple';
import Avatar from '@material-ui/core/Avatar';
import axios from "axios";
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import {withRouter} from "react-router";


const userURL = '/api/user/user/';

export class UserInfo extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      name: '',
      email: '',
      avatar: ''
    };
  }

  componentDidMount() {
    axios
      .get(userURL)
      .then((response) =>{
        this.setState({
          name: response.data.user.login,
          email: response.data.user.email,
          avatar: response.data.user.avatar
        });
      })
      .catch((error) => console.log(error));
  }

  render(){
    const { classes } = this.props;
    return(
      <Card>
        <CardContent className={classes.orangeAvatar}>
          <Avatar className={classes.avatar} src={this.state.avatar}></Avatar>
          <Typography variant="h5" component="h2" className={classes.name}>
            {this.state.name}
          </Typography>
          <Typography color="textSecondary">
            {this.state.email}
          </Typography>
        </CardContent>
      </Card>
    )
  }
}

export default withStyles(styles)(withRouter(UserInfo));