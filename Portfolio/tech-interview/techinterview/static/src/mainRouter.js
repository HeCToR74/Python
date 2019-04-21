/* eslint max-len: ["error", { "ignoreStrings": true }]*/

import React from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';
import Home from './components/Home';
import Section from 'src/components/question/Section';
import CreateInterview from 'src/components/interview/CreateInterview';
import InterviewList from './components/interview/InterviewList';
import Stage from 'src/components/question/Stage';
import StageList from 'src/components/question/StageList';
import SectionList from 'src/components/question/SectionList';
import Question from './components/question/Question';
import QuestionList from './components/question/QuestionList';
import {CandidatePool} from 'src/components/pool/CandidatePool';
import DepartmentList from 'src/components/department/DepartmentList';
import {Department} from 'src/components/department/Department';
import {ExpertPool} from 'src/components/expertpool/ExpertPool';
import InterviewResults from 'src/components/interview/results/InterviewResults';
import Profile from 'src/components/auth/Profile';
import Analytics from './components/analytics/Analytics';
import Grade from 'src/components/feedback/Grade';
import GradeList from 'src/components/feedback/GradeList';


import getMuiTheme from 'material-ui/styles/getMuiTheme';
import {ExpertResult} from 'src/components/expertpool/ExpertResult';

const mainStyle = {
  paddingTop: getMuiTheme().appBar.height,
  paddingLeft: '5%',
  paddingRight: '5%',
};

/**
 * Main router of application
 */
export default class MainRouter extends React.Component {
  /**
   * @return {*} - Switch components
   */
  render() {
    return (
      <main id="container"  style={mainStyle}>
        <Switch>
          <Route path='/home/' component={Home} />
          <Route path='/expert/res/:id' component={ExpertResult} />
          <Route path='/home' component={Home} />
          <Route path='/grade/new' component={Grade} />
          <Route path='/grade/:id' component={Grade} />
          <Route path='/grade' component={GradeList} />
          <Route path='/interview/new' component={CreateInterview} />
          <Route path='/interview/:id' component={CreateInterview} />
          <Route path='/interview' component={InterviewList} />
          <Route path='/stage/new/' component={Stage} />
          <Route path='/stage/:id' component={Stage} />
          <Route path='/stage/' component={StageList} />
          <Route path='/section/new' component={Section} />
          <Route path='/section/:id' component={Section} />
          <Route path='/section/' component={SectionList} />
          <Route path='/question/new' component={Question} />
          <Route path='/question/:id' component={Question} />
          <Route path='/question/' component={QuestionList} />
          <Route path='/test/:id' component={CandidatePool} />
          <Route path='/department/new' component={Department} />
          <Route path='/expert/:id' component={ExpertPool}/>
          <Route path='/department/:id' component={Department} />
          <Route path='/result/:id' component={InterviewResults}/>
          <Route path='/department/' component={DepartmentList} />
          <Route path='/profile/' component={Profile} />
          <Route path='/analytics/' component={Analytics} />
          <Redirect path='*' to='/home/' />
        </Switch>
      </main>
    );
  }
}
