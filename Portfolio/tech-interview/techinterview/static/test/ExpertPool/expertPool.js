import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {ExpertPool} from "src/components/expertpool/ExpertPool";

configure({ adapter: new Adapter() });

describe('Expert Pool component', () => {
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
    }
  });

  const setup = () => shallow(<ExpertPool {...props} />);

  context('Pool rendering', () => {
    it('Show spinner if no data', () => {
      const component = setup();
      expect(component.find('WithStyles(CircularProgress)').length).to.equal(1);
    });
  });
});