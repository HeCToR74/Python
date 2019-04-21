import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {ExpertTable} from "src/components/expertpool/ExpertTable";

configure({ adapter: new Adapter() });

describe('Expert Table component', () => {
  let props;
  beforeEach(() => {
    class LocalStorageMock {
      constructor() {
        this.store = {};
      }

      clear() {
        this.store = {};
      }

      getItem(key) {
        return this.store[key] || null;
      }

      setItem(key, value) {
        this.store[key] = value.toString();
      }

    }
    global.localStorage = new LocalStorageMock;

    props = {
      match: {
        params: {
          id: null
        }
      },
      data: [
        {id:1, name: 'question1'},
        {id:2, name: 'question2'},
        {id:3, name: 'question3'}
      ]
    }
  });

  const setup = () => shallow(<ExpertTable {...props} />);

  context('Table rendering', () => {
    it('Headers is renders', () => {
      const component = setup();
      expect(component.find('h1').length).to.equal(1);
    });
  });
});