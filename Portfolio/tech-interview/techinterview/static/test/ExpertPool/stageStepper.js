import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {StageStepper} from "src/components/expertpool/StageStepper";

configure({ adapter: new Adapter() });

describe('Stage Stepper component', () => {
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
      stages: ['stage1', 'stage2']
    }
  });

  const setup = () => shallow(<StageStepper {...props} />);

  context('Component rendering', () => {
    it('Steps is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(Step)').length).to.equal(2);
    });
  });
});