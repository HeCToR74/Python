import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {TestCell} from "src/components/pool/TestCell";

configure({ adapter: new Adapter() });

describe('Test Cell component', () => {
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
      questionID: 1,
      name: 'test_question',
    }
  });

  const setup = () => shallow(<TestCell {...props} />);

  context('Form rendering', () => {
    it('TableRowColumn is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(TableCell)').length).to.equal(3);
    });

    it('DropDown is renders', () => {
      const component = setup();
      expect(component.find('SelfEstimateDropDown').length).to.equal(1);
    });

    it('Toggle is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(Switch)').length).to.equal(1);
    });
  });


  context('Object handling', () => {
    it('DropDown is correct', () => {
      const component = setup();
      expect(component.find('SelfEstimateDropDown').prop('selected')).to.equal(1);
    });
    it('Toggle is correct', () => {
      const component = setup();
      expect(component.find('WithStyles(Switch)').prop('checked')).to.equal(false);
    });
  });
});