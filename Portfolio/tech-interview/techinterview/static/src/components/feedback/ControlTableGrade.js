import React from 'react';
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import IconButton from "@material-ui/core/IconButton";
import DeleteIcon from "@material-ui/icons/Delete";
import EditIcon from "@material-ui/icons/Edit";
import {NavLink} from 'react-router-dom';
import axios from 'axios';
import Snackbar from "@material-ui/core/Snackbar";
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Paper from '@material-ui/core/Paper';
import Draggable from 'react-draggable';


/**
 * Table for show up all grades
 */
export default class ControlTableGrade extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      grades: [],
      snackbar: false,
      message: '',
      open: false,
    };
  }

  /**
   * Fetch grades when component was accessed
   */
  componentDidMount() {
    axios('/api/feedback/grades').then((response) =>{
      this.setState({grades: response.data});
    });
  }


  /**
   * Send DELETE request for specified section.
   * Show message when it deleted and remove it from list
   */
  deleteGrade(index) {
    axios.delete('/api/feedback/grades/'+index).then((response) => {
      const grades = this.state.grades.filter((m) => m.id !== index);
      this.setState({
        grades: grades,
        message: 'Grade was deleted',
        snackbar: true,
        open: false
      });
    }
    );
  }

  handleClickOpen() {
    axios('/api/feedback/grades').then((response) =>{
      this.setState({ open: true });
    });
  }

  handleClose() {
    axios('/api/feedback/grades').then((response) =>{
        this.setState({ open: false });
    });
  }

  /**
   * Render filled table
   * @return {*} - return component
   */
  render() {
    return (
      <div>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell
                tooltip="The Id">Id</TableCell>
              <TableCell
                tooltip="The Name">Name</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.grades.map( (row, index) => (
              <TableRow key={index}>
                <TableCell>{row.name}</TableCell>
                <TableCell>
                  <NavLink to={'/grade/'+row.id}>
                    <IconButton aria-label="Edit">
                      <EditIcon />
                    </IconButton>
                  </NavLink>
                  <IconButton aria-label="Delete"
                        onClick={this.handleClickOpen.bind(this)}>
                    <DeleteIcon />
                  </IconButton>
                  <Dialog
                      open={this.state.open}
                      onClose={this.handleClose.bind(this)}
                      aria-labelledby="responsive-dialog-title"
                    >
                      <DialogTitle id="responsive-dialog-title">{"Are you sure you want to delete the grade?"}</DialogTitle>

                      <DialogActions>
                        <Button onClick={this.handleClose.bind(this)} color="primary">
                          No
                        </Button>
                        <Button onClick={() => this.deleteGrade(row.id)} color="primary" autoFocus>
                          Yes
                        </Button>
                      </DialogActions>
                    </Dialog>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <Snackbar
          open={this.state.snackbar}
          message={this.state.message}
          autoHideDuration={4000}
        />
      </div>
    );
  }
}
