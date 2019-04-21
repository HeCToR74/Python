import React from 'react';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import SwipeableViews from 'react-swipeable-views';
import CircularProgress from '@material-ui/core/CircularProgress';
import axios from 'axios';
import Snackbar from '@material-ui/core/Snackbar';
import {StageStepper} from 'src/components/expertpool/StageStepper';

/**
 * Candidate form component for testing
 */
export class ExpertPool extends React.Component {
  /**
   * Set up questions data and current slide id
   * @param {*} props - data from parent object
   */
  constructor(props) {
    super(props);
    this.state = {
      value: 0,
      depart: null,
      openMessage: false,
      hideDelay: 2000,
    };
  }

  /**
   * Fetch component data from API
   */
  componentWillMount() {
    axios('/api/interviews/'+this.props.match.params.id).then((response) =>{
      this.setState({depart: response.data.department});
    });
  }

  /**
   * Change tab view
   * @param {*} value - current section id
   */
  handleChange(event, value) {
    this.setState({value});
  }

  handleChangeIndex(index) {
    this.setState({value: index});
  }

  /**
   * If stepper send signal 'Next page' -> turn on next page
   */
  triggerNextTab() {
    this.setState({slideIndex: this.state.slideIndex+1});
  }

  /**
   * Submit data wh
en finish button was pressed
   */
  triggerFinish() {
    const questionsID = [];
    Object.keys(this.state.depart.sections).map((value) => {
      Object.keys(this.state.depart.sections[value]).map((question) => {
        this.state.
depart.sections[value][question]
            .map((q) => questionsID.push(q.id));
      });
    });
    const bulk = questionsID.map((question) => {
      return {
        comment: localStorage.getItem(question+'_comment'),
        grade: parseInt(localStorage.getItem(question+'_grade')),
        interview: this.props.match.params.id,
        question: question,
      };
    });
    axios.post('/api/feedback/comments/bulk', bulk).then((response) => {
      localStorage.clear();
    });
    this.setState({openMessage: true});
    setTimeout(() => this.props.history.push(`/expert/res/`
      + this.props.match.params.id),
    this.state.hideDelay);
  }

  /**
   * Render spinner if data not loaded yet
   * else render full form with data
   * @return {*} - form
   */
  render() {
    if (!this.state.depart) {
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
        <Tabs
          value={this.state.value}
          onChange={this.handleChange.bind(this)}
          indicatorColor="primary"
          textColor="primary"
          variant="fullWidth"
        >
          {Object.keys(this.state.depart.sections)
              .map((section, index) => <Tab key={index}
                label={section}
                value={index} />)}
        </Tabs>
        <SwipeableViews
          index={this.state.value}
          onChangeIndex={this.handleChangeIndex.bind(this)}
        >
          {Object.keys(this.state.depart.sections).map((section, index) => {
            return (<div key={index}>
              <StageStepper stages={this.state.depart.sections[section]}
                interview={this.props.match.params.id}
                isLast={
                  index === Object.keys(this.state.depart.sections).length-1
                }
                changeTrigger={this.triggerNextTab.bind(this)}
                endTrigger={this.triggerFinish.bind(this)}
              />
            </div>);
          })}
        </SwipeableViews>
        <Snackbar
          open={this.state.openMessage}
          message={'Expert review were saved'}
          autoHideDuration={this.state.hideDelay}
        />
      </div>
    );
  }
}
