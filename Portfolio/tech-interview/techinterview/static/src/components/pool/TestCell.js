import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import SelfEstimateDropDown from 'src/components/pool/SelfEstimateDropDown';
import Switch from '@material-ui/core/Switch';

/**
 * Question component in TestTable
 */
export class TestCell extends React.Component {
  /**
   * Set up default parameters for question
   * @param {*} props - data from parent component
   */
  constructor(props) {
    super(props);
    this.state = {
      gradeID: 1,
      toggleStatus: false,
    };
  }

  /**
   * Change value if dropdown was changed
   * @param {*} value - value from dropdown component
   */
  handleDropdown(value) {
    this.setState({gradeID: value});
  }

  /**
   * Change toggleStatus if toggle was pressed
   * @param {*} event - DOM event
   * @param {*} isInputChecked - toggle status
   */
  handleToggle(event, isInputChecked) {
    this.setState({toggleStatus: isInputChecked});
  }

  /**
   * If candidate already answered on question
   * load his answer from localstorage
   */
  componentWillMount() {
    if (
      (parseInt(localStorage.getItem(this.props.questionID+'_grade')) !== 0) &&
        (localStorage.getItem(this.props.questionID+'_toggle') !== null)
    ) {
      this.setState({
        gradeID: parseInt(localStorage
            .getItem(this.props.questionID+'_grade')),
        toggleStatus: Boolean(localStorage
            .getItem(this.props.questionID+'_toggle')),
      });
    }
  }

  /**
   * Change data in localstorage if candidate answered on question
   */
  componentDidUpdate() {
    localStorage.setItem(this.props.questionID+'_grade',
        this.state.gradeID);
    localStorage.setItem(this.props.questionID+'_toggle',
        this.state.toggleStatus);
  }

  /**
   * Render question
   * @return {*} - TableRow with question
   */
  render() {
    return (
      <TableRow key={this.props.questionID}>
        <TableCell>{this.props.name}</TableCell>
        <TableCell><Switch onChange={this.handleToggle.bind(this)}
                           color="primary"
                           checked={this.state.toggleStatus}/>
        </TableCell>
        <TableCell><SelfEstimateDropDown onChange={this.handleDropdown.bind(this)}
          selected={this.state.gradeID}/>
        </TableCell>
      </TableRow>
    );
  }
}
