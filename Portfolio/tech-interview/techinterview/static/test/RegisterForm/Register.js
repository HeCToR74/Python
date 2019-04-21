import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {Register} from '../../src/components/auth/Register';

configure({ adapter: new Adapter() });

describe('Register component', () => {
  let props;

  beforeEach(() => {
    props = {
      match: {
        params: {
          id: null
        }
      },
      classes: {
        button: "Register-button-75",
        display: "Register-display-72",
        fontFamily: "Register-fontFamily-64",
        height: "Register-height-65",
        labelField: "Register-labelField-73",
        margin: "Register-margin-67",
        marginLeft: "Register-marginLeft-68",
        minWidth: "Register-minWidth-69",
        position: "Register-position-70",
        root: "Register-root-76",
        textAlign: "Register-textAlign-71",
        textField: "Register-textField-74",
        width: "Register-width-66",
      },
    }
  });

  const setup = () => shallow(<Register {...props} />);

  context('Initial state of create form', () => {
      
    it('Objects is renders', () => {
      const component = setup();
      expect(component.find('TextField').length).to.equal(6);
      expect(component.find('#Paper').length).to.equal(1);
      expect(component.find('form').length).to.equal(1);
      expect(component.find('#Button').length).to.equal(1);
      expect(component.find('h3').length).to.equal(5);
      expect(component.find('#Snackbar').length).to.equal(1);
      expect(component.find('#Dialog').length).to.equal(1);
      expect(component.find('#DialogTitle').length).to.equal(1);
      expect(component.find('#DialogContent').length).to.equal(1);
      expect(component.find('#DialogContentText').length).to.equal(1);
      expect(component.find('#DialogActions').length).to.equal(1);
      expect(component.find('#OK').length).to.equal(1);
    });

    it('Button is disabled', () => {
      const component = setup();
      expect(component.find('#Button').prop('disabled')).to.equal(true);
    });

    it('TextFields is empty', () => {
      const component = setup();
      expect(component.find('#login').prop('value')).to.equal('');
      expect(component.find('#password').prop('value')).to.equal('');
      expect(component.find('#confirm').prop('value')).to.equal('');
      expect(component.find('#first').prop('value')).to.equal('');
      expect(component.find('#last').prop('value')).to.equal('');
      expect(component.find('#email').prop('value')).to.equal('');
    });

  });

  context('Form functionality', () => {

    it('Button is enabled', () => {
      const component = setup();

      component.find('#login').simulate('change', {target: {value: "user"}});
      component.find('#password').simulate('change', {target: {value: "qwe123Q!"}});
      component.find('#confirm').simulate('change', {target: {value: "qwe123Q!"}});
      component.find('#first').simulate('change', {target: {value: "first"}});
      component.find('#last').simulate('change', {target: {value: "last"}});
      component.find('#email').simulate('change', {target: {value: "user@mail.com"}});

      expect(component.find('#Button').prop('disabled')).to.equal(false);
    });

    it('TextFields is changed', () => {
      const component = setup();

      component.find('#login').simulate('change', {target: {value: "user"}});
      component.find('#password').simulate('change', {target: {value: "qwe123Q!"}});
      component.find('#confirm').simulate('change', {target: {value: "qwe123Q!"}});
      component.find('#first').simulate('change', {target: {value: "first"}});
      component.find('#last').simulate('change', {target: {value: "last"}});
      component.find('#email').simulate('change', {target: {value: "user@mail.com"}});
      
      expect(component.state().inputLogin.value).to.equal('user');
      expect(component.state().inputPass.value).to.equal('qwe123Q!');
      expect(component.state().inputConfirm.value).to.equal('qwe123Q!');
      expect(component.state().inputFirst.value).to.equal('first');
      expect(component.state().inputLast.value).to.equal('last');
      expect(component.state().inputEmail.value).to.equal('user@mail.com');
    });

  });

});
