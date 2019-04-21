import React from 'react';
import MainRouter from './mainRouter';
import SignRouter from './signRouter';
import Header from './components/header/Header';
import Sign from './components/auth/Sign';
import axios from 'axios';


const isUserLoggedIn = () => document.cookie.indexOf('sessionid') !== -1;
/**
 * Main layout of project
 * Also redirecting between routers
 */
export default class Layout extends React.Component {
  /**
     * Redirecting user dependence on authorization state
     * @return {*} - Route to necessary router
     */
  render() {
    return (
      isUserLoggedIn() ?
        <div>
          <Header/>
          <MainRouter/>
        </div> :
        <div>
          <Sign/>
          <SignRouter/>
        </div>
    );
  }
}
