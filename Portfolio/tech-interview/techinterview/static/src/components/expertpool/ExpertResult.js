import React from 'react';
import PropTypes from 'prop-types';
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';
import {withRouter} from "react-router-dom";
import DropDownRes from 'src/components/expertpool/DropDownRes';
import TextField from '@material-ui/core/TextField';
import Tooltip from '@material-ui/core/Tooltip';
import Button from "@material-ui/core/Button";
import CircularProgress from "@material-ui/core/CircularProgress";
import { listLevel, englishLevel, listHighPotential, listPotential } from 'src/constants.js';


const  URLpost = '/api/interviews/res/';

export class ExpertResult extends React.Component {
  /**
   * Set up questions data and current slide id
   * @param {*} props - data from parent object
   */

  constructor(props) {
    super(props);
    this.state = {
      slideIndex: 0,
      depart: null,
      openMessage: false,
      hideDelay: 2000,
      multilineField: {
        value: '',
      },
      summaryOfQualification: {
        value: '',
      },
      years_of_experience: {
        value: '',
      },
      level: {
        value: '',
      },
      level_com: {
        value: '',
      },
      gaps: {
        value: '',
      },
      gaps_com: {
        value: '',
      },
      technical_english: {
        value: '',
      },
      technical_english_com: {
        value: '',
      },
      high_potential: {
        value: '',
      },
      high_potential_com: {
        value: '',
      },
      potentially_hire: {
        value: '',
      },
      potentially_hire_com: {
        value: '',
      },
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  componentWillMount() {
    axios.get('/api/feedback/results/'+ this.props.match.params.id)
      .then((response) =>
        this.setState({
          level: {
            value: response.data.total,
          },
        })
      );
  }
  setEnabledButton() {
    if (this.state.summaryOfQualification.value !== ''
      && this.state.years_of_experience.value !==''
      && this.state.level.value !== ''
      && this.state.level_com.value !== ''
      && this.state.gaps.value !== ''
      && this.state.gaps_com.value !==''
      && this.state.technical_english.value !== ''
      && this.state.technical_english_com.value !==''
      && this.state.high_potential.value !==''
      && this.state.high_potential_com.value !== ''
      && this.state.potentially_hire.value !==''
      && this.state.potentially_hire_com.value !==''){
      return false;
    } else {
      return true;
    }
  };
  handleChange(evt) {
    this.setState({ [evt.target.name]: {value: evt.target.value} });
  };
  handleSubmit(evy) {
    const intData = {
      'summary_of_qualification': this.state.summaryOfQualification.value,
      'years_of_experience': this.state.years_of_experience.value,
      'level': this.state.level.value,
      'level_com': this.state.level_com.value,
      'gaps': this.state.gaps.value,
      'gaps_com': this.state.gaps_com.value,
      'technical_english': this.state.technical_english.value,
      'technical_english_com': this.state.technical_english_com.value,
      'high_potential': this.state.high_potential.value,
      'high_potential_com': this.state.high_potential_com.value,
      'potentially_hire': this.state.potentially_hire.value,
      'potentially_hire_com': this.state.potentially_hire_com.value,
      'f_interview_id': this.props.match.params.id,
    };
    axios.post((URLpost + this.props.match.params.id + '/'), intData)
      .then((res) => {
        this.props.history.push('/home/');
      })
      .catch((error) => {
        console.log(error);
      });
  };

  /**
   * Render spinner if data not loaded yet
   * else render full form with data
   * @return {*} - form
   */
  render() {
    if (this.state.level.value === '') {
      return (
        <CircularProgress size={120}
          thickness={2.7}
          style={{
            position: 'absolute',
            left: '50%',
            top: '50%'}}/>);
    }
    return (
      <Paper>
        <Table >
          <TableHead>
            <TableRow>
              <TableCell><h1>Candidate Qualification</h1></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell style={styles.nameCategory}>
                <strong>Summary of Qualification</strong><br/>
                (information about candidate:
                <strong>general opinion</strong>, level,
                <strong>main technologies</strong>,
                types of projects, <strong>preferred projects</strong>,
                <strong>main business domains</strong>,
                <strong>strong sides,</strong> leading experience,
                risks,  communication during interview)
              </TableCell>
              <TableCell>
                <TextField
                  required
                  id="summary_of_qualification"
                  name={'summaryOfQualification'}
                  onChange={this.handleChange}
                  defaultValue=""
                  multiline
                  value={this.state.summaryOfQualification.value}
                  rows ="4"
                  style={styles.MultilineField}
                  margin="normal"
                />
              </TableCell>
            </TableRow>
            <TableRow >
              <TableCell style={styles.nameCategory}>
                <strong>Years of Experience</strong></TableCell>
              <TableCell style={styles.autoField}>
                <TextField
                  required
                  id="years_of_experience"
                  margin="normal"
                  name={'years_of_experience'}
                  onChange={this.handleChange}
                  value={this.state.years_of_experience.value}
                />
              </TableCell>
              <TableCell style={styles.fieldExp}>
              </TableCell>
            </TableRow>
            <TableRow >
              <TableCell style={styles.nameCategory}>
                <strong>Level</strong><br/>
                (according requirements from knowledge model)
              </TableCell>
              <Tooltip placement="left-start" title="Set candidate's lavel" >
                <TableCell style={styles.autoField}>
                  <DropDownRes
                    handleChange={this.handleChange}
                    selectValue={this.state.level.value}
                    name ='level'
                    id="level"
                    values= {listLevel}
                  />
                </TableCell>
              </Tooltip>
              <Tooltip placement="left-start"
                       title='If level is different from
                "automatically generated expert level",
                 please provide explanation about your decision.
                 Such explanation will help to calibrate
                 "automatically generated level" formula.'>
                <TableCell style={styles.fieldExp}>
                  <TextField
                    required
                    name={'level_com'}
                    id="level_com"
                    value={this.state.level_com.value}
                    margin="normal"
                    onChange={this.handleChange}
                  /></TableCell>
              </Tooltip>
            </TableRow>
            <TableRow>
              <TableCell style={styles.nameCategory}>
                <strong>Gaps</strong><br/>
                (scope of gaps to promote on level,
                estimate how much time will take to fix gaps)
              </TableCell>
              <Tooltip placement="left-start"
                       title="Estimation how much time is needed to promote to the next level.
                          Example: '3-4 months to Intermedidate level'">
                <TableCell style={styles.autoField}> 
                  <TextField
                    required
                    id="gaps"
                    value={this.state.gaps.value}
                    margin="normal"
                    onChange={this.handleChange}
                    name={'gaps'}
                  /> 
                </TableCell>
              </Tooltip>
              <Tooltip placement="left-start"
                       title={'Describe scope of critical' +
                       ' and optional gaps to be fixed with estimates.\n' +
                       '\n' +'Example:' +
                       'Critical areas:\n' +'* HTML5 Forms; Web-components (2 weeks)\n' +
                       '* CSS3: SCSS or less; Bootstrap (2 months)\n' +
                       '\n' +
                       'Optional areas:\n' +
                       '* SDLC: distributed teams coordination and collaboration,' +
                       ' engineering process planning,' +
                       ' Scrum vs Kanban applicability (1 month)\n' +
                       '\n'}>
                <TableCell style={styles.fieldExp}>
                  <TextField
                    required
                    value={this.state.gaps_com.value}
                    id="gaps_com"
                    margin="normal"
                    name={'gaps_com'}
                    onChange={this.handleChange}
                  />
                </TableCell>
              </Tooltip>
            </TableRow>
            <TableRow >
              <TableCell style={styles.nameCategory}>
                <strong>Technical English</strong><br/>
                (communication skills in English with native speakers)
              </TableCell>
              <Tooltip placement="left-start" title='Set the English level'>
                <TableCell style={styles.autoField}>
                  <DropDownRes
                    values={englishLevel}
                    handleChange={this.handleChange}
                    selectValue={this.state.technical_english.value}
                    id="technical_english"
                    name={'technical_english'}
                  /> </TableCell>
              </Tooltip>
              <Tooltip placement='left-start'
                       title={'Provide how much time candidate has experience in communication with native speakers,' +
                       ' listening and speaking skills.\n' +
                       '\n' +'Example: Can provide information in English. Has low experience with communication with native speakers' +
                       ' (~6 months), so there can be issues with understanding on calls with client.\n'}>
                <TableCell style={styles.fieldExp}>
                  <TextField
                    required
                    id="technical_english_com"
                    // label="Uncontrolled"
                    defaultValue=""
                    margin="normal"
                    name={'technical_english_com'}
                    onChange={this.handleChange}
                    value={this.state.technical_english_com.value}
                  />
                </TableCell>
              </Tooltip>
            </TableRow>
            <TableRow>
              <TableCell style={styles.nameCategory}>
                <strong>High potential</strong><br/>
                (estimation how quickly candidate will grow as software engineer)
              </TableCell>
              <TableCell style={styles.autoField}>
                <DropDownRes
                  values={listHighPotential}
                  handleChange={this.handleChange}
                  selectValue={this.state.high_potential.value}
                  name={'high_potential'}
                  id="high_potential"
                /> </TableCell>
              <Tooltip placement="left-start" title={'If the first cell is \'high potential\' or ' +
              '\'low potential\' please provide explanation here.\n' + '\n'}>
                <TableCell style={styles.fieldExp}>
                  <TextField
                    required
                    id="high_potential_com"
                    value={this.state.high_potential_com.value}
                    margin="normal"
                    name={'high_potential_com'}
                    onChange={this.handleChange}
                  />
                </TableCell>
              </Tooltip>
            </TableRow>
            <TableRow>
              <TableCell style={styles.nameCategory}>
                <strong>Potentially Hire</strong><br/>
                (notify if there are some objections to hire candidate,
                like <strong>attitude</strong>,
                <strong> soft skills</strong>, ability to work in team, etc.)
              </TableCell>
              <Tooltip placement="left-start"
                       title='Set "not hire" if you
                        do not recommend
                       hire candidate into company
                      (lazy, very low potential, aggressive,
                      etc), disregarding
                      his technical level'>
                <TableCell style={styles.autoField}>
                  <DropDownRes
                    values={listPotential}
                    handleChange={this.handleChange}
                    selectValue={this.state.potentially_hire.value}
                    name={'potentially_hire'}
                    id="potentially_hire"
                  /> </TableCell>
              </Tooltip>
              <Tooltip placement="left-start"
                       title={'If the first cell says ' +
                       '\'not hire\' please provide your explanation here.\n' +
                       '\n'}>
                <TableCell style={styles.fieldExp}>
                  <TextField
                    required
                    onChange={this.handleChange}
                    id="potentially_hire_com"
                    value={this.state.potentially_hire_com.value}
                    margin="normal"
                    name={'potentially_hire_com'}
                  />
                </TableCell>
              </Tooltip>
            </TableRow>
            <TableRow>
              <TableCell>
              </TableCell>
              <TableCell>
              </TableCell>
              <TableCell style={styles.fieldExp}>
                <Button
                  id='saveChanges'
                  variant='contained'
                  onClick={this.handleSubmit}
                  color='primary'
                  disabled={this.setEnabledButton()}>
                  Save changes
                </Button>
              </TableCell>
            </TableRow>

          </TableBody>
        </Table>
      </Paper>
    );
  }
}