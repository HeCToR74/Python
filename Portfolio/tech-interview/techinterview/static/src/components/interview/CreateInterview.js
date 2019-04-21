import React from "react";
import axios from "axios";
import moment from "moment";
import Moment from "moment";
import PropTypes from "prop-types";
import { withRouter } from "react-router-dom";
import { styles } from './../../styles/styles';
import { withStyles } from '@material-ui/core/styles';
import { RegisterModal } from "src/components/auth/RegisterModal";
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";
import Select from "@material-ui/core/Select";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import MenuItem from "@material-ui/core/MenuItem";
import Snackbar from "@material-ui/core/Snackbar";
import AddIcon from "@material-ui/icons/Add";
import IconButton from "@material-ui/core/IconButton";
import DateFnsUtils from "@date-io/date-fns";
import { MuiPickersUtilsProvider, DateTimePicker } from "material-ui-pickers";
import TextField from "@material-ui/core/TextField";
import {MapModal} from "src/components/interview/MapModal";
import { tempDate, date, currDate } from 'src/constants.js';


const postURL = "/api/interviews/";

/**
 * Creates a form to create Section
 */
export class CreateInterview extends React.Component {
  /**
   * Constructor of class
   * @param {props} props - Properties of object
   */
  constructor(props) {
    super(props);
    this.state = {
      field: {
        value: "",
        error: ""
      },

      depField: [],
      canField: [],
      expField: [],

      DepartmentValue: "",
      CandidateValue: "",
      ExpertValue: "",
      DataValue: currDate,

      candidateDialog: false,
      expertDialog: false,
      mapDialog: false,
      snackbar: {
        open: false,
        message: ""
      },

      submitButton: {
        disabled: true,
        label: "Create interview"
      },
      coords: {lat: null, lng: null},
      location: null,

      pushMethod: "POST"
    };
  }

  /**
   * Change handler for selectfield
   * @param {event} event - Send event from object
   */
  handleChangeDepartment(event, index) {
    this.setState({
      DepartmentValue: event.target.value,
      snackbar: {
        message: "",
        open: false
      }
    });
  }
  /**
   * Change handler for selectfield
   * @param {event} event - Send event from object
   */
  handleChangeCandidate(event, index) {
    this.setState({
      CandidateValue: event.target.value,
      snackbar: {
        message: "",
        open: false
      }
    });
  }
  /**
   * Change handler for selectfield
   * @param {event} event - Send event from object
   */
  handleChangeExpert(event, index) {
    this.setState({
      ExpertValue: event.target.value,
      snackbar: {
        message: "",
        open: false
      }
    });
  }
  /**
   * Change handler for selectfield
   * @param {event} newDate - Send event from object
   */

  handleDateChange(newDate) {
    this.setState({
      DataValue: moment(newDate).format("YYYY-MM-DD HH:mm:ssZZ")
    });
  }

  /**
   * Submit handler to send data to API and show message
   * @param {event} event - Send event from object
   */
  handleSubmit(event) {
    event.preventDefault();
    const serverport = {
      department: this.state.DepartmentValue,
      candidate: this.state.CandidateValue,
      expert: this.state.ExpertValue,
      interview_date: this.state.DataValue,
      latitude: this.state.coords.lat,
      longitude: this.state.coords.lng,
      location: this.state.location,
    };
    if (!this.props.match.params.id){
      axios.post(postURL, serverport).then(res => {
      this.setState({
        snackbar: {
          message: "Interview was created",
          open: true
        }},
      this.props.history.push("/interview"));})
    } else {
    axios.put(postURL+this.props.match.params.id, serverport).then(res => {
      this.setState({
        snackbar: {
          message: "Interview was created",
          open: true
        }
      });
      this.props.history.push("/interview");
    });}
  }

  deptab() {
    return this.state.depField.map(function(object) {
      return (
        <MenuItem key={object.id} value={object.id}>
          {object.name}
        </MenuItem>
      );
    });
  }
  cantab() {
    return this.state.canField.map(function(object) {
      return (
        <MenuItem key={object.auth.id} value={object.auth.id}>
          {`${object.auth.first_name} ${object.auth.last_name} (${
            object.auth.email
          })`}
        </MenuItem>
      );
    });
  }
  expTab() {
    return this.state.expField.map(function(object) {
      return (
        <MenuItem key={object.auth.id} value={object.auth.id}>
          {`${object.auth.first_name} ${object.auth.last_name} (${
            object.auth.email
          })`}
        </MenuItem>
      );
    });
  }

  /**
   * Data loader page
   */
  componentWillMount() {
    axios
      .get("/api/departments/")
      .then(response => {
        this.setState({ depField: response.data });
      })
      .catch(function(error) {});

    axios
      .get("/api/user/user/?role=candidate")
      .then(response => {
        this.setState({ canField: response.data });
      })
      .catch(function(error) {});
    axios
      .get("/api/user/user/?role=expert")
      .then(response => {
        this.setState({ expField: response.data });
      })
      .catch(function(error) {});

    if (this.props.match.params.id) {
      axios("/api/interviews/" + this.props.match.params.id).then(response => {
        this.setState({
          DepartmentValue: response.data.department.id,
          CandidateValue: response.data.candidate.auth.id,
          ExpertValue: response.data.expert.auth.id,
          pushMethod: "PUT",
          coords: {lat: response.data.latitude , lng: response.data.longitude},
          location: response.data.location,
          pushURL: "/api/interviews/" + this.props.match.params.id,
          submitButton: { label: "Edit interview" }
        });
      });
    }
  }

  /**
   * Close Snackbar message
   */
  handleClose() {
    this.setState({ snackbar: false });
  }

  setEnabledButton() {
    return (
      !this.state.DepartmentValue ||
      !this.state.CandidateValue ||
      !this.state.ExpertValue
    );
  }

  handleOpenCandidateDialog(event) {
    event.preventDefault();

    this.setState({ candidateDialog: true });
  }
  handleCloseCandidateDialog(event) {
    event.preventDefault();
    this.setState({ candidateDialog: false });
  }
  handleSubmitCandidateDialog(id) {
    axios("/api/user/user/?role=candidate")
      .then(response => {
        this.setState({ canField: response.data, CandidateValue: id });
      })
      .catch(function(error) {});
    this.setState({ candidateDialog: false });
  }

  handleOpenExpertDialog(event) {
    event.preventDefault();

    this.setState({ expertDialog: true });
  }
  handleCloseExpertDialog(event) {
    event.preventDefault();
    this.setState({ expertDialog: false });
  }
  handleSubmitExpertDialog(id) {
    axios("/api/user/user/?role=expert")
      .then(response => {
        this.setState({ expField: response.data, ExpertValue: id });
      })
      .catch(function(error) {});
    this.setState({ expertDialog: false });
  }
  handleOpenMapDialog(event) {
    event.preventDefault();
    this.setState({ mapDialog: true });
  }
  handleCloseMapDialog(event) {
    event.preventDefault();
    this.setState({ mapDialog: false });
  }
  handleMapSubmit(coords, location){
    this.setState({mapDialog: false, coords, location});
  }
  /**
   * Render HTML form with handlers
   * @return {React} - Render form to page
   */
  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <Paper className={classes.root} elevation={5}>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <h1>Create new interview:</h1>
            <br />
            <h3>Department</h3>

            <FormControl id="FormControl" className={classes.formControl}>
              <Select
                id="department"
                value={this.state.DepartmentValue}
                onChange={this.handleChangeDepartment.bind(this)}
              >
                {this.deptab()}
              </Select>
              <FormHelperText>Choose a department</FormHelperText>
            </FormControl>

            <br />
            <h3>Candidate</h3>
            <div style={{ display: "block" }}>
              <FormControl id="FormControl" className={classes.formControl}>
                <Select
                  id="candidate"
                  value={this.state.CandidateValue}
                  onChange={this.handleChangeCandidate.bind(this)}
                >
                  {this.cantab()}
                </Select>
                <FormHelperText>Choose a candidate</FormHelperText>
              </FormControl>

              <IconButton
                aria-label="Delete"
                style={{ position: "absolute" }}
                onClick={this.handleOpenCandidateDialog.bind(this)}
              >
                <AddIcon />
              </IconButton>
            </div>
            <br />
            <div style={{ display: "block" }}>
              <h3>Expert</h3>
              <br />

              <FormControl id="FormControl" className={classes.formControl}>
                <Select
                  id="expert"
                  value={this.state.ExpertValue}
                  onChange={this.handleChangeExpert.bind(this)}
                >
                  {this.expTab()}
                </Select>
                <FormHelperText>Choose an expert</FormHelperText>
              </FormControl>

              <IconButton
                aria-label="Delete"
                style={{ position: "absolute" }}
                onClick={this.handleOpenExpertDialog.bind(this)}
              >
                <AddIcon />
              </IconButton>
            </div>
            <br />
            <TextField
              onClick={this.handleOpenMapDialog.bind(this)}
              label="Location(Optional)"
              value={this.state.location}
              margin="normal"
            />

            <br />
            <h3>Date of interview</h3>

            <MuiPickersUtilsProvider utils={DateFnsUtils}>
              <DateTimePicker
                value={this.state.DataValue}
                onChange={this.handleDateChange.bind(this)}
                minutesStep={5}
                autoOk
                minDate={date}
                showTodayButton
              />
              <FormHelperText style={{ textAlign: "center" }}>
                Choose date of interview
              </FormHelperText>
            </MuiPickersUtilsProvider>

            <br />
            <br />
            <Button
              id="Button"
              variant="contained"
              color="primary"
              type="submit"
              disabled={this.setEnabledButton()}
            >
              {this.state.submitButton.label}
            </Button>
          </form>
          <Snackbar
            open={this.state.snackbar.open}
            message={this.state.snackbar.message}
            autoHideDuration={4000}
            onClose={this.handleClose.bind(this)}
          />
          <br />
          <br />
          <div>
            <RegisterModal
              open={this.state.candidateDialog}
              onClose={this.handleCloseCandidateDialog.bind(this)}
              onSubmit={this.handleSubmitCandidateDialog.bind(this)}
              role={"Candidate"}
            />
            <RegisterModal
              open={this.state.expertDialog}
              onClose={this.handleCloseExpertDialog.bind(this)}
              onSubmit={this.handleSubmitExpertDialog.bind(this)}
              role={"Expert"}
            />
            <MapModal
              open={this.state.mapDialog}
              onClose={this.handleCloseMapDialog.bind(this)}
              onSubmit={this.handleMapSubmit.bind(this)}
            />
          </div>
        </Paper>
      </React.Fragment>
    );
  }
}

CreateInterview.propTypes = {
  value: PropTypes.instanceOf(Moment)
};

CreateInterview.defaultProps = {
  value: null
};

export default withStyles(styles)(withRouter(CreateInterview));
