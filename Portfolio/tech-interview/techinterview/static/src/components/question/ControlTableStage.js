import React from 'react';
import axios from 'axios';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import Snackbar from '@material-ui/core/Snackbar';

const URL = '/api/questions/stages/';

export class ControlTableStage extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      stages: [],
      snackbar: false,
      message: '',
    };
  }
  
  deleteSection(index) {
    axios.delete(URL + index).then(() => {
      const stages = this.state.stages.filter((m) => m.id !== index);
      this.setState({
        stages: stages,
        message: 'Stage was deleted',
        snackbar: true,
      });
    }
    );
  }
  componentWillMount() {
    axios(URL).then((response) => {
      this.setState({ stages: response.data });
    });
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
        <Table id='Table' height={'auto'}>
          <TableHead id='TableHead'>
            <TableRow>
              <TableCell
                tooltip="Name">Name</TableCell>
              <TableCell
                tooltip="Actions">Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody id='TableBody'>
            {this.state.stages.map((row, index) => (
              <TableRow key={index}>
                <TableCell>{row.name}</TableCell>
                <TableCell>
                  <IconButton aria-label="Delete"
                    onClick={() => this.deleteSection(row.id)}>
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
          autoHideDuration={2000}
          onClose={this.handleClose.bind(this)}
        />
      </Paper>
    );
  }
}
