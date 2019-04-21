import React from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import Paper from '@material-ui/core/Paper';


export class ControlTableDepartment extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      departments: [],
      snackbar: false,
      message: '',
      pushURL: '/api/departments/',
    };
  }


  componentDidMount() {
    axios.get(this.state.pushURL).then((response) => {
      this.setState({ departments: response.data });
    });
  }


  deleteDepartment(index) {
    axios.delete(this.state.pushURL + index).then((response) => {
      const departments = this.state.departments.filter((m) => m.id !== index);
      this.setState({
        departments: departments,
        message: 'Department was deleted',
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

  render() {
    return (
      <Paper>
        <Table height={'auto'}>
          <TableHead>
            <TableRow>
              <TableCell 
                tooltip="The Name">Name</TableCell >
              <TableCell 
                tooltip="The Actions">Actions</TableCell >
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.departments.map((row, index) => (
              <TableRow key={index}>
                <TableCell >{row.name}</TableCell >
                <TableCell >
                  <NavLink to={'/department/' + row.id}>
                    <IconButton aria-label="Edit">
                      <EditIcon />
                    </IconButton>
                  </NavLink>
                  <IconButton aria-label="Delete"
                    onClick={() => this.deleteDepartment(row.id)}>
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
          autoHideDuration={4000}
          onClose={this.handleClose.bind(this)}
        />
      </Paper>
    );
  }
}
