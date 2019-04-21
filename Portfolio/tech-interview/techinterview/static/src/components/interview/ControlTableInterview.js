import React from 'react';
import axios from 'axios';
import {withRouter, NavLink} from 'react-router-dom';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import PhotoCamera from '@material-ui/icons/PhotoCamera';
import Assignment from '@material-ui/icons/Assignment'
import EditIcon from '@material-ui/icons/Edit';
import Snackbar from '@material-ui/core/Snackbar';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import TablePagination from '@material-ui/core/TablePagination';
import NavigationExpandLess from "material-ui/svg-icons/navigation/expand-less";
import NavigationExpandMore from "material-ui/svg-icons/navigation/expand-more";
import moment from "moment"


function searchingFor(term) {
  return function(x) {
    return (
      x.candidate_email.toLowerCase().includes(term.toLowerCase()) || !term
    );
  };
}

function desc(a, b, orderBy) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

/**
 *
 * Table for show up all interviews
 */
export class ControlTableInterview extends React.Component {
  constructor(props) {
    super(props);
    this.sorted = { age: true, name: true };
    this.state = {
      interviews: [],
      page: 1,
      rowsPerPage: 5,
      rowsPerPageOptions: [5, 10, 15, 20, 25, ],

      term: "",
      snackbar: false,
      message: "",
      open: false,
      columnToSort: "",
      sortDirection: "desc",

      pagination: {
        count: 0,
        next: null,
        previous: null,
      },
    };
    
    this.stableSort.bind(this);
    this.getSorting.bind(this);
  }

  componentDidMount() {
    axios("/api/interviews/?list=true&page_size=" + this.state.rowsPerPage)
    .then(response => {
      this.setState({
        interviews: response.data.results,
        pagination: {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        }
      });
    });
  }

  deleteInterview(index) {
    axios.delete("/api/interviews/" + index).then(response => {
      const interviews = this.state.interviews.filter(m => m.id !== index);
      this.setState({
        interviews: interviews,
        message: "Interview was deleted",
        snackbar: true,
      });
    });
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({ snackbar: false });
  }

  searchHandler(event) {
    this.setState({ term: event.target.value });
  }

  stableSort(array, cmp) {
    const stabilizedThis = array.map((el, index) => [el, index]);
    stabilizedThis.sort((a, b) => {
      const order = cmp(a[0], b[0]);
      if (order !== 0) return order;
      return a[1] - b[1];
    });
    return stabilizedThis.map(el => el[0]);
  }

  getSorting(order, orderBy) {
    return order === "desc"
      ? (a, b) => desc(a, b, orderBy)
      : (a, b) => -desc(a, b, orderBy);
  }

  /**
   * Change handler for inputLogin
   * @param {*} event - current event
   * @param {*} page - current page
   */
  handleChangePage(event, page) {
    axios("/api/interviews/?list=true&page_size="
        + this.state.rowsPerPage + "&page=" + (page+1))
      .then(response => {
      this.setState({
        interviews: response.data.results,
        pagination: {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        },
        page: page,
      });
    });
  };

  /**
   * Change handler for inputLogin
   * @param {*} event - current event
   */
  handleChangeRowsPerPage(event) {
    axios("/api/interviews/?list=true&page_size=" + event.target.value)
      .then(response => {
      this.setState({
        interviews: response.data.results,
        pagination: {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        },
        page: 0,
        rowsPerPage: event.target.value,
      });
    });
  };

 /**
   * Render filled table
   * @return {*} - return component
   */
  render() {
    const { term } = this.state;
    const header = [
      {
        name: "First name",
        prop: "candidate"
      },
      {
        name: "Expert Name",
        prop: "expert"
      },
      {
        name: "Interview Date",
        prop: "interview_date"
      },
      {
        name: "Location",
        prop: "location"
      },
      {
        name: "Actions",
        prop: "Actions"
      }
    ];
    return (
      <Paper id='Paper'>
          <form>
            <TextField
              id="1"
              helperText="Search for candidate email"
              onChange={this.searchHandler.bind(this)}
              style={{marginLeft: "20px"}}
              value={term}
            />
          </form>
        <Table id='Table'>
          <TableHead id='TableHead'>
            <TableRow>
              {header.map((x, i) => (
                <TableCell key={i}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                    }}
                    onClick={() => {
                      this.setState({ columnToSort: x.prop });
                    }}
                  >
                    <span>{x.name}</span>
                    {this.state.columnToSort === x.prop ? (
                this.state.sortDirection === "asc" ? (
                  <NavigationExpandLess />
                ) : (
                  <NavigationExpandMore />
                )
              ) : null}
                  </div>
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody id='TableBody'>
            {this.stableSort(
              this.state.interviews,
              this.getSorting("asc", this.state.columnToSort)
            )
              .filter(searchingFor(term))
              .map((row, index) => (
                <TableRow key={index}>
                  <TableCell>
                    {row.candidate}
                    <b>({row.candidate_email})</b>
                  </TableCell>
                  <TableCell>
                    {row.expert}
                    <b>({row.expert_email})</b>
                  </TableCell>
                  <TableCell>
                    {moment(row.interview_date).format(
                      "MMMM Do YYYY, h:mm:ss a"
                    )}
                  </TableCell>
                  <TableCell>
                    {row.location || 'None'}
                  </TableCell>
                  <TableCell>
                    <div>
                      <NavLink to={"/interview/" + row.id}>
                        <IconButton aria-label="Edit">
                          <EditIcon />
                        </IconButton>
                      </NavLink>
                      <NavLink to={row.status !== "scheduled"? "/result/" + row.id: "#"}>
                        <IconButton
                          aria-label="Edit"
                          disabled={row.status === "scheduled"}
                        >
                          <Assignment />
                        </IconButton>
                      </NavLink>
                      <IconButton
                        aria-label="Delete"
                        disabled={row.status !== "scheduled"}
                        onClick={() => this.deleteInterview(row.id)}
                      >
                        <DeleteIcon />
                      </IconButton>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
          </TableBody>
        </Table>
        <TablePagination id='TablePagination'
          rowsPerPageOptions={this.state.rowsPerPageOptions}
          rowsPerPage={this.state.rowsPerPage}
          // component="div"
          count={this.state.pagination.count}
          page={this.state.page}
          onChangePage={this.handleChangePage.bind(this)}
          onChangeRowsPerPage={this.handleChangeRowsPerPage.bind(this)}
        />
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

export default withRouter(ControlTableInterview);
