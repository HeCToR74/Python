import React from 'react';
import {expect} from 'chai';
import {shallow} from 'enzyme';
import {Section} from '../../src/components/question/Section';

import {configure} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({adapter: new Adapter()});

describe('Section component', () => {
  let props;

  beforeEach(() => {
    props = {
      match: {
        params: {
          id: null,
        },
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
    };
  });

  const setup = () => shallow(<Section {...props} />);

  context('Initial state of create form', () => {
    it('Objects is renders', () => {
      const component = setup();
      expect(component.find('TextField').length).to.equal(1);
      expect(component.find('#Paper').length).to.equal(1);
      expect(component.find('form').length).to.equal(1);
      expect(component.find('#Button').length).to.equal(1);
    });

    it('Buttons is disabled', () => {
      const component = setup();
      expect(component.find('#Button').prop('disabled')).to.equal(true);
    });

    it('TextField is empty', () => {
      const component = setup();
      expect(component.find('TextField').prop('value')).to.equal('');
    });

    it('Submit method is POST', () => {
      const component = setup();
      expect(component.state().pushMethod).to.equal('POST');
    });

    it('Submit endpoint is correct', () => {
      const component = setup();
      expect(component.state().pushURL).to.equal('/api/questions/sections/');
    });
  });

  context('Form style', () => {
    it('Name div is correct', () => {
      const component = setup();
      // expect(component.find('#nameDiv').get(0).props.style).to.deep.equal({
      //   display: 'block',
      //   margin: 'auto',
      //   paddingBottom: '2em',
      // });
    });
    it('TextField is correct', () => {
      const component = setup();
      // expect(component.find('TextField').get(0).props.style).to.deep.equal({
      //   minWidth: '35%',
      // });
    });
  });


  context('Form functionality', () => {
    it('TextField is changed', () => {
      const component = setup();
      component.find('TextField').simulate('change', {target: {value: 'text'}});
      expect(component.state().textField.value).to.equal('text');
    });
  });
});
