import React from 'react';
import { styles } from './../../../styles/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import axios from 'axios';
import Divider from '@material-ui/core/Divider';
import CircularProgress from '@material-ui/core/CircularProgress';
import SwipeableViews from 'react-swipeable-views';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const gradesAPI = '/api/feedback/grades?dict=true';

/**
 * Table for show up all sections
 */
export default class InterviewResults extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 0,
      level: '',
      candidate: '',
      department: null,
      interviewExist: true,
      resultsExist: true,
      statuses: {},
      answers: {},
      comments: {},
      grades: {},
    };
    const id = this.props.match.params.id;
    this.interviewAPI = `/api/interviews/${id}`;
    this.commentsAPI = `/api/feedback/comments?interview_id=${id}`;
    this.answersAPI = `/api/feedback/answers?interview_id=${id}`;
    this.resultsAPI = `/api/feedback/results/${id}`;
  }

  /**
   * Fetch sections when component was accessed
   */
  async componentDidMount() {
    const grades = await axios(gradesAPI);
    const interview = await axios(this.interviewAPI);
    const results = await axios(this.resultsAPI);
    const comments = await axios(this.commentsAPI);
    const answers = await axios(this.answersAPI);

    const name = `${interview.data.candidate.auth
      .first_name} ${interview.data.candidate.auth.last_name}`;

    this.setState({
      grades: grades.data,
      candidate: name,
      department: interview.data.department,
      comments: comments.data,
      answers: answers.data,
      level: results.data.total,
      statuses: results.data.levels,
    });
  }

  /**
   * Change tabs when user clicks
   * @param {*} value - Index of tabs
   */
  handleChange(event, value) {
    this.setState({value});
  }

  handleChangeIndex(index) {
    this.setState({value: index});
  }
  /**
   * Render filled table
   * @return {*} - return component
   */
  render() {
    if (this.state.department === null) {
      return (
        <CircularProgress size={120}
          thickness={2.7}
          style={{
            position: 'absolute',
            left: '50%',
            top: '50%'}}/>);
    }

    return (
      <div>
        <div style={styles.inter_res.header}>
          <h3 style={styles.inter_res.expertLevel}>
            <span style={styles.inter_res.span}>
              Automatically generated expert level:
            </span> {this.state.level}
          </h3>
          <h3 style={styles.inter_res.candidateName}>
            <span
              style={styles.inter_res.span}>Candidate:</span> {this.state.candidate}
          </h3>
        </div>
        <Tabs
          value={this.state.value}
          onChange={this.handleChange.bind(this)}
          indicatorColor="primary"
          textColor="primary"
          variant="fullWidth"
        >
          {Object.keys(this.state.department.sections)
              .map((section, index) => <Tab key={index}
                label={section}
                value={index} />)}
        </Tabs>
        <SwipeableViews
          index={this.state.value}
          onChangeIndex={this.handleChangeIndex.bind(this)}
        >
          {Object.keys(this.state.department.sections)
            .map(((section, index) => {
            return (<div key={index}>
              {Object.keys(this.state.department.sections[section])
                .map((stage, index) => {
                return (<div key={index}><h2
                    style={styles.inter_res.stage}>{stage}</h2>
                  <Divider style={styles.inter_res.divider}/>
                  <Table height={'auto'}>
                    <TableHead displaySelectAll={false} adjustForCheckbox={false}>
                      <TableRow>
                        <TableCell>Question</TableCell>
                        <TableCell>Like to do</TableCell>
                        <TableCell>Candidate's grade</TableCell>
                        <TableCell>Validated grade</TableCell>
                        <TableCell>Expert comment</TableCell>
                        <TableCell>Generated level</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody displayRowCheckbox={false}>
                      {this.state.department.sections[section][stage]
                        .map((question) =>
                        (<TableRow key={question.id}>
                          <TableCell>
                            {question.name}
                          </TableCell>
                          <TableCell>
                            {this.state.answers[question.id]
                              .answer_like ? 'Yes' : 'No'}
                          </TableCell>
                          <TableCell>
                            {this.state.grades[this.state.answers[question.id]
                              .grade]}
                          </TableCell>
                          <TableCell>
                            {this.state.grades[this.state.comments[question.id]
                              .validated_grade]}
                          </TableCell>
                          <TableCell>
                            {this.state.comments[question.id].comment ?
                          this.state.comments[question.id].comment :
                              <span style={styles.inter_res.span}>None</span>}
                          </TableCell>
                          <TableCell style={styles.inter_res.generatedLevel}>
                            {this.state.statuses[question.id]}
                          </TableCell>
                        </TableRow>)
                      )
                      }
                    </TableBody>
                  </Table>
                </div>
                );
              })
              }
            </div>);
          }))}
        </SwipeableViews>
      </div>);
  }
}