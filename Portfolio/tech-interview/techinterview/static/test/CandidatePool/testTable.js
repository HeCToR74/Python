import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {TestCell} from "src/components/pool/TestCell";
import {TestTable} from "src/components/pool/TestTable";

configure({ adapter: new Adapter() });

describe('Test Table component', () => {
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

  const setup = () => shallow(<TestTable {...props} />);

  context('Table rendering', () => {
    it('Table is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(Table)').length).to.equal(1);
    });

    it('Headers is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(TableCell)').length).to.equal(3);
    });

    it('Questions is renders', () => {
      const component = setup();
      expect(component.find('TestCell').length).to.equal(3);
    });

    it('TableHead is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(TableHead)').length).to.equal(1);
    });

    it('TableBody is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(TableBody)').length).to.equal(1);
    });
  });
});