import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { Department } from '../../src/components/department/Department';
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';


configure({ adapter: new Adapter() });

describe('Department component', () => {
    let props;

  beforeEach(() => {
    props = {
      match: {
        params: {
          id: null,
        },
      },
    };
  });

   const setup = () => shallow(<Department {...props}/>);

  context('Initial state of create form', () => {

    it('Objects is renders', () => {
      const component = setup();
      expect(component.find('TextField').length).to.equal(1);
      expect(component.find('#questions').length).to.equal(1);
      expect(component.find('form').length).to.equal(1);
      expect(component.find('#Button').length).to.equal(1);
    });

    it('Button is disabled', () => {
      const component = setup();
      expect(component.find('#Button').prop('disabled')).to.equal(true);
    });

    it('TextField and SelectField are empty', () => {
      const component = setup();
      expect(component.state().textField.value).to.equal('');
      expect(component.state().values).to.deep.equal([]);
    });

  });


  context('Form functionality', () => {

    it('Button is disabled', () => {
      const component = setup();

      component.find('#department').simulate('change', {target: {value: "Python"}});
      component.setState({ values:[1,2]});


      expect(component.find('#Button').prop('disabled')).to.equal(true);
    });

    it('TextField and SelectField are changed', () => {
      const component = setup();

      component.find('#department').simulate('change', {target: {value: "Python"}});
      component.setState({ values:[1,2]});


      expect(component.state().textField.value).to.equal("Python");
      expect(component.state().values).to.deep.equal([1,2]);

    });

  });

});
