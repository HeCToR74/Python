import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import {ExpertCell} from 'src/components/expertpool/ExpertCell';
import axios from 'axios';

/**
 * Render table with questions
 * @param {*} props - data from parent object
 * @return {*} - render object
 */
export class ExpertTable extends React.Component {
  /**
   * Default react constructor
   * @param {*} props - parent component objects
   */
  constructor(props) {
    super(props);
    this.state = {
      answers: {},
    };
  }

  /**
   * Load candidate data
   */
  componentWillMount() {
    axios('/api/feedback/answers?interview_id='+this.props.interview)
        .then((response) => this.setState({answers: response.data}));
  }

  /**
   * Render table when answers was loaded
   * @return {*} - table with candidate answers
   */
  render() {
    if (Object.keys(this.state.answers).length === 0) {
      return (
        <h1>The candidate has not answered the questions yet</h1>);
    }
    return (
      <div>
        <Table height={'500px'}>
          <TableHead>
            <TableRow>
              <TableCell>Question</TableCell>
              <TableCell>User Like to do</TableCell>
              <TableCell>User Grade</TableCell>
              <TableCell>Expert Grade</TableCell>
              <TableCell>Expert Comment</TableCell>
            </TableRow>
          </TableHead>
          <TableBody >
            {this.props.data.map((question) => (
              <ExpertCell key={question.id}
                questionID={question.id}
                name={question.name}
                answer={this.state.answers[question.id]}/>
            ))}
          </TableBody>
        </Table>
      </div>
    );
  }
}
