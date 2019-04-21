import React from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';
import Login from './components/auth/Login';
import Register from './components/auth/Register';
import PasswordReset from './components/auth/PasswordReset';
import PasswordResetConfirm from './components/auth/PasswordResetConfirm';

/**
 * Router if user not authorized
 */
export default class SignRouter extends React.Component {
  /**
     * @return {*} - Switch components
     */
  render() {
    return (
      <main>
        <Switch>
          <Route path='/login/' component={Login} />
          <Route path='/register/' component={Register}/>
          <Route path='/password_reset/confirm/:token' component={PasswordResetConfirm} />
          <Route path='/password_reset/' component={PasswordReset}/>
          <Redirect path='*' to='/login/'/>
        </Switch>
      </main>
    );
  }
}
