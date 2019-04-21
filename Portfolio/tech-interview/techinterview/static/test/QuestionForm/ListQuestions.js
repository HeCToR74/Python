import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { ControlTableStage } from '../../src/components/question/ControlTableQuestion';
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import {ControlTableQuestion} from "src/components/question/ControlTableQuestion";

configure({ adapter: new Adapter() });

describe('ControlTableQuestion component', () => {
  let props;

  beforeEach(() => {
    props = {
      match: {
        params: {
          id: null
        }
      }
    }
  });

  const setup = () => shallow(<ControlTableQuestion {...props} />);

    context('Initial state of create form', () => {

      it('Objects is renders', () => {
        const component = setup();
        expect(component.find('#Table').length).to.equal(1);
        expect(component.find('#TableHead').length).to.equal(1);
        expect(component.find('#TableBody').length).to.equal(1);
        expect(component.find('#Snackbar').length).to.equal(1);
      });

      it('Snackbar is disabled', () => {
        const component = setup();
        expect(component.find('#Snackbar').prop('open')).to.equal(false);
      });
    });
});
