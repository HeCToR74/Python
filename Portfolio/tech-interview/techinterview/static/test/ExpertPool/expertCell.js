import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {ExpertCell} from "src/components/expertpool/ExpertCell";

configure({ adapter: new Adapter() });

describe('Expert Cell component', () => {
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
      answer: {answer_like: true, grade:2}
    }
  });

  const setup = () => shallow(<ExpertCell {...props} />);

  context('Form rendering', () => {
    it('TableRowColumn is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(TableCell)').length).to.equal(5);
    });

    it('DropDowns is renders', () => {
      const component = setup();
      expect(component.find('SelfEstimateDropDown').length).to.equal(2);
    });

    it('Toggle is renders', () => {
      const component = setup();
      expect(component.find('WithStyles(Switch)').length).to.equal(1);
    });

    it('TextField is renders', () => {
      const component = setup();
      expect(component.find('TextField').length).to.equal(1);
    });
  });



  context('Candidate answers', () => {
    it('DropDown is disabled', () => {
      const component = setup();
      expect(component.find('#CandidateComment').prop('disabled')).to.equal(true);
    });
    it('Toggle is disabled', () => {
      const component = setup();
      console.log(component.debug());
      expect(component.find('WithStyles(Switch)').prop('disabled')).to.equal(true);
    });
    it('DropDown is correct', () => {
      const component = setup();
      expect(component.find('#CandidateComment').prop('selected')).to.equal(2);
    });
    it('Switch is correct', () => {
      const component = setup();
      expect(component.find('WithStyles(Switch)').prop('checked')).to.equal(true);
    });
  });

    context('Expert answers functionality', () => {
    it('TextField is changed', () => {
      const component = setup();
      component.find('TextField').simulate('change', {target: {value: "good!"}});
      expect(component.state().comment).to.equal('good!');
    });
    it('ExpertGrade is changed', () => {
      const component = setup();
      component.find('#ExpertComment').simulate('change', 3);
      expect(component.state().gradeID).to.equal(3);
    });
  });
});