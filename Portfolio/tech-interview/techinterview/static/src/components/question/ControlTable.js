import React from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import Snackbar from '@material-ui/core/Snackbar';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

/**
 * Table for show up all sections
 */
export class ControlTable extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      sections: [],
      snackbar: false,
      message: '',
    };
  }

  /**
   * Fetch sections when component was accessed
   */
  componentDidMount() {
    axios('/api/questions/sections').then((response) => {
      this.setState({ sections: response.data });
    });
  }

  /**
   * Send DELETE request for specified section.
   * Show message when it deleted and remove it from list
   */
  deleteSection(index) {
    axios.delete('/api/questions/sections/' + index).then((response) => {
      const sections = this.state.sections.filter((m) => m.id !== index);
      this.setState({
        sections: sections,
        message: 'Section was deleted',
        snackbar: true,
      });
    }
    );
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
        <Table height={'auto'}>
          <TableHead>
            <TableRow>
              <TableCell
                tooltip="The Name">Name</TableCell>
              <TableCell
                tooltip="The Actions">Actions</TableCell>
            </TableRow>
          </TableHead >
          <TableBody>
            {this.state.sections.map((row, index) => (
              <TableRow key={index}>
                <TableCell >{row.name}</TableCell >
                <TableCell >
                  <NavLink to={'/section/' + row.id}>
                    <IconButton aria-label="Edit">
                      <EditIcon aria-label="Edit">edit_icon</EditIcon>
                    </IconButton>
                  </NavLink>
                  <IconButton aria-label="Delete"
                    onClick={() => this.deleteSection(row.id)}>
                    <DeleteIcon />
                  </IconButton>
                </TableCell >
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <Snackbar
          open={this.state.snackbar}
          message={this.state.message}
          autoHideDuration={2000}
          onClose={this.handleClose.bind(this)}
        />
      </Paper>
    );
  }
}
