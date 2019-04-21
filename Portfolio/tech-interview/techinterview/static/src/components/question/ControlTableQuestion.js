import React from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import {withRouter} from 'react-router-dom';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import Snackbar from '@material-ui/core/Snackbar';
import Paper from '@material-ui/core/Paper';

/**
 * Table for show up all questions
 */
export class ControlTableQuestion extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      questions: [],
      snackbar: false,
      message: '',
    };
  }

  /**
   * Fetch questions when component was accessed
   */
  componentDidMount(event) {
    axios.get('/api/questions/questions/')
      .then((response) => {
        this.setState({ questions: response.data });
      })
      .catch((error) => console.log(error))
  }

  /**
   * Send DELETE request for specified question.
   * Show message when it deleted and remove it from list
   */
  deleteQuestion(index) {
    axios.delete('/api/questions/questions/' + index).then((response) => {
      const questions = this.state.questions.filter((m) => m.id !== index);
      this.setState({
        questions: questions,
        message: 'Question was deleted',
        snackbar: true,
      });
    });
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({snackbar: false });
  }  

  /**
   * Render filled table
   * @return {*} - return component
   */
  render() {
    return (
      <Paper>
        <Table id='Table' height={'auto'}>
          <TableHead id='TableHead'>
            <TableRow>
              <TableCell
                tooltip="The Name">Name</TableCell>
              <TableCell
                tooltip="Hint">Hint</TableCell>
              <TableCell
                tooltip="Stage">Stage</TableCell>
              <TableCell
                tooltip="The Actions">Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody id='TableBody'>
            {this.state.questions.map((row, index) => (
              <TableRow key={index}>
                <TableCell>{row.name}</TableCell>
                <TableCell>{row.hint}</TableCell>
                <TableCell>{row.stage.name}</TableCell>
                <TableCell>
                  <NavLink to={'/question/' + row.id}>
                    <IconButton aria-label="Edit">
                      <EditIcon />
                    </IconButton>
                  </NavLink>
                  <IconButton aria-label="Delete"
                    onClick={() => this.deleteQuestion(row.id)}>
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <Snackbar id='Snackbar'
          open={this.state.snackbar}
          message={this.state.message}
          autoHideDuration={4000}
          onClose={this.handleClose.bind(this)}
        />
      </Paper>
    );
  }
}

export default withRouter(ControlTableQuestion);
