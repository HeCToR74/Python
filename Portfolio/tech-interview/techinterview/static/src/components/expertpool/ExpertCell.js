import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import GradeDropDown from 'src/components/expertpool/GradeDropDown';
import Switch from '@material-ui/core/Switch';
import TextField from '@material-ui/core/TextField';

/**
 * Question component in TestTable
 */
export class ExpertCell extends React.Component {
  /**
   * Set up default parameters for question
   * @param {*} props - data from parent component
   */
  constructor(props) {
    super(props);
    this.state = {
      gradeID: 1,
      toggleStatus: false,
      comment: '',
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
   * Set comment field changes
   * @param {*} event - DOM event with changed data
   */
  handleComment(event) {
    this.setState({comment: event.target.value});
  }

  /**
   * Change data in localstorage if expert chose grade or write comment
   */
  componentDidUpdate() {
    localStorage.setItem(this.props.questionID+'_grade',
        this.state.gradeID);
    localStorage.setItem(this.props.questionID+'_comment',
        this.state.comment);
  }
  /**
   * Render question
   * @return {*} - TableRow with question
   */
  render() {
    if (!this.props.answer) {
      return <TableRow/>;
    }
    return (
      <TableRow key={this.props.questionID}>
        <TableCell>{this.props.name}</TableCell>
        <TableCell><Switch onChange={this.handleToggle.bind(this)}
          checked={this.props.answer.answer_like} color="primary"
          disabled={true}/>
        </TableCell>
        <TableCell><GradeDropDown selected={this.props.answer.grade}
          id={'CandidateComment'}
          disabled={true}
        />
        </TableCell>
        <TableCell><GradeDropDown onChange={this.handleDropdown.bind(this)}
          id={'ExpertComment'}
          selected={this.state.gradeID}
          disabled={false}/>
        </TableCell>
        <TableCell>
          <TextField
            onChange={this.handleComment.bind(this)}
            floatingLabelText="Comment"
            floatingLabelFixed={true}/><br />
        </TableCell>
      </TableRow>
    );
  }
}
