import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {Sign} from "../src/components/auth/Sign";

configure({ adapter: new Adapter() });

describe('Tabs component', () => {
  let props;

  beforeEach(() => {
    props = {
      match: {
        params: {
          id: null
        }
      },
      history: {
        location: {
          pathname: 'login',
        }
      }
    }
  });

  const setup = () => shallow(<Sign {...props} />);

  context('Initial state of Tabs', () => {

    it('Tabs was rendered', () => {
      const component = setup();
      expect(component.find('#Tabs').length).to.equal(1);
    });

    it('Tab are renders', () => {
      const component = setup();
      expect(component.find('#Tab').length).to.equal(3);
    });

  });
});