import React, {Component} from 'react';
import axios from 'axios';
import * as d3 from "d3";
import { BarChart } from "react-d3-components";
//npm install react-d3-components
import Select from '@material-ui/core/Select';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import MenuItem from '@material-ui/core/MenuItem';
import Chip from 'material-ui/Chip';
import {blueA100, orange500, lightBlue800} from 'material-ui/styles/colors';
import { InitialDataBarChart, ConstDayMonthYear, InitialCurrentType } from 'src/constants.js';

const styles = {
  chip: {
    margin: 'auto',
    display: 'flex',
    flexWrap: 'wrap',
  },
};

/**
 * Creates a form to create Analytics
 */
class Analytics extends React.Component {
   /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
    constructor(props) {
        super(props);

        this.state = {
            currentType: InitialCurrentType,
            currentRecruiter: "",
            DayMonthYear: ConstDayMonthYear,
            data: [],
            recruiter: [],
            dataBarChart: InitialDataBarChart,
        };

        this.style = {
          fontFamily: 'Roboto',
          nameDiv: {
            display: 'block',
            margin: 'auto',
            paddingBottom: '2em',
          },
          nameTextField: {
            postiton: 'absolute',
          },
          formControl: {
            minWidth: '15%',
          },
        };

        //this.handleChangeSelecting = this.handleChangeSelecting.bind(this);
        //this.handleChangeRecruiter = this.handleChangeRecruiter.bind(this);
    };

  handleChangeSelecting(event, value) {
    this.setState({currentType: value.key}, () => {
        if (this.state.currentType == "7 Days") {
            this.setState({dataBarChart: this.state.data['all_data'][this.state.currentRecruiter]['day_data']});
        }
        if (this.state.currentType == "Month") {
            this.setState({dataBarChart: this.state.data['all_data'][this.state.currentRecruiter]['month_data']});
        }
        if (this.state.currentType == "Year") {
            this.setState({dataBarChart: this.state.data['all_data'][this.state.currentRecruiter]['year_data']});
        }
    });
  }

  handleChangeRecruiter(event, value) {
      this.setState({currentRecruiter: value.key}, () => {
        if (this.state.currentType == "7 Days") {
            this.setState({dataBarChart: this.state.data['all_data'][this.state.currentRecruiter]['day_data']});
        }
        if (this.state.currentType == "Month") {
            this.setState({dataBarChart: this.state.data['all_data'][this.state.currentRecruiter]['month_data']});
        }
        if (this.state.currentType == "Year") {
            this.setState({dataBarChart: this.state.data['all_data'][this.state.currentRecruiter]['year_data']});
        }
    });
  }

  tabSelecting() {
    return this.state.DayMonthYear.map(function(object) {
      return <MenuItem
                    key={object}
                    value={object}>
                {object}
             </MenuItem>
    });
  }

  tabRecruiter() {
    return this.state.recruiter.map(function(object) {
      return <MenuItem
                    key={object.auth.username}
                    value={object.auth.username}>
                {object.auth.username}
             </MenuItem>
    });
  }

  /**
   * Data loader if page loads with id in URL
   */
  componentWillMount() {
    axios.get('/api/interviews/analytics/')
        .then((response) =>{
          this.setState({
            data: response.data,
            currentRecruiter: response.data['username'],
            dataBarChart: response.data['all_data'][response.data['username']]['day_data'],
          });
        })
        .catch(function(error) {
          console.log(error);
        });
    axios.get('/api/user/user/?role=recruiter')
        .then((response) =>{
          this.setState({
            recruiter: response.data,
          });
        })
        .catch(function(error) {
          console.log(error);
        });

  }

  /**
   * Render HTML form with handlers
   * @return {React} - Render form to page
   */
  render(){
    return (
    <div>
        <div style={this.style}> Recruiter: {this.state.currentRecruiter}</div>
        <div>
            <FormControl style={this.style.formControl}>
                <Select
                    //floatingLabelText="Selection of period"
                    value={this.state.currentType}
                    onChange={this.handleChangeSelecting.bind(this)}>
                    {this.tabSelecting()}
                </Select>
            </FormControl>
            <FormControl style={this.style.formControl}>
                <Select
                    //floatingLabelText="Selection of recruiter"
                    value={this.state.currentRecruiter}
                    onChange={this.handleChangeRecruiter.bind(this)}>
                    {this.tabRecruiter()}
                </Select>
            </FormControl>
        </div>
        <BarChart
          data={this.state.dataBarChart}
          width={1200}
          height={600}
          margin={{ top: 100, bottom: 50, left: 150, right: 10 }}
          groupedBars
        />
        <div style={styles.chip}>
            <Chip backgroundColor={blueA100}>
              Date of creation of interview
            </Chip>
            <Chip backgroundColor={orange500}>
              Date of interviewing
            </Chip>
            <Chip backgroundColor={lightBlue800}>
             Completion date of interview
            </Chip>
        </div>
    </div>

  )}
}

export default Analytics;

// import Chip from '@material-ui/core/Chip';
// import Avatar from '@material-ui/core/Avatar';

//           <Chip label="Date of creation of interview" color='primary' />
//           <Chip label="Date of interviewing" color='secondary' />
//           <Chip
//             label="Completion date of interview"
//             // color='#1769aa'
//             avatar={<Avatar src="/static/images/avatar/1.jpg" />}
//             variant='outlined' />