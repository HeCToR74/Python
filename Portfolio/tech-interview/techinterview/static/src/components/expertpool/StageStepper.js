import React from 'react';
import Button from '@material-ui/core/Button';
import Step from '@material-ui/core/Step';
import Stepper from '@material-ui/core/Stepper';
import StepButton from '@material-ui/core/StepButton';
import ArrowForward from '@material-ui/icons/ArrowForward';
import {ExpertTable} from 'src/components/expertpool/ExpertTable';

/**
 * Component for Stages
 */
export class StageStepper extends React.Component {
  /**
   * Set up first step
   * @param {*} props - parent data
   */
  constructor(props) {
    super(props);

    this.state = {
      stepIndex: 0,
      stepContent: Object.keys(props.stages).map(function(value) {
        return (<ExpertTable interview={props.interview} data={props.stages[value]} />);
      }),
      endLabel: 'Next Stage',
    };
  }

  /**
   * Get questions from cache
   * @param {number} stepIndex - index of step
   * @return {*} - array of questions
   */
  getStepContent(stepIndex) {
    return this.state.stepContent[stepIndex];
  }

  /**
   * Render new stage by button click
   */
  handleNext() {
    const {stepIndex} = this.state;

    if (stepIndex < 2) {
      this.setState({stepIndex: stepIndex + 1});
    }
  }

  /**
   * Render previous stage by button click
   */
  handlePrev() {
    const {stepIndex} = this.state;

    if (stepIndex > 0) {
      this.setState({stepIndex: stepIndex - 1});
    }
  }

  /**
   * Handler for finish button
   */
  handleFinish() {
    if (this.props.isLast) {
      this.props.endTrigger();
      return;
    }
    this.props.changeTrigger();
  }

  /**
   * Checker if section is last
   */
  componentDidMount() {
    if (this.props.isLast) {
      this.setState({endLabel: 'Finish'});
    }
  }

  /**
   * Render stepper
   * @return {*} - load component
   */
  render() {
    const {stepIndex} = this.state;
    return (
      <div style={{width: '100%', maxWidth: 700, margin: 'auto'}}>
        <Stepper activeStep={stepIndex}
                 connector={<ArrowForward/>}
                 style={{justifyContent: 'space-between'}}>
          {Object.keys(this.props.stages).map((value, index) => {
            return (<Step key={index} disabled={false}>
              <StepButton onClick={() => {
                this.setState({stepIndex: index});
              }}>
                {value}
              </StepButton>
            </Step>);
          })}
        </Stepper>

        {this.getStepContent(stepIndex)}

        <div style={{marginTop: 24, marginBottom: 12}}>
          <Button
            disabled={stepIndex === 0}
            onClick={this.handlePrev.bind(this)}
            style={{marginRight: 12}}
          >Back</Button>
          <Button
            variant="contained"
            color="primary"
            onClick={stepIndex === 2 ? this.handleFinish.bind(this) : this.handleNext.bind(this)}
          >{stepIndex === 2 ? this.state.endLabel : 'Next'}</Button>
        </div>
      </div>
    );
  }
}
