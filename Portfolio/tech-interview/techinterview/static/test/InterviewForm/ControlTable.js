import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { ControlTableInterview } from '../../src/components/interview/ControlTableInterview';
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';


configure({ adapter: new Adapter() });

describe('TableInterview component', () => {
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

    const setup = () => shallow(<ControlTableInterview {...props} />);
    
    it('Objects is renders', () => {
        const component = setup();
        expect(component.find('#Paper').length).to.equal(1);
        expect(component.find('TextField').length).to.equal(1);
        expect(component.find('#Table').length).to.equal(1);
        expect(component.find('#TableHead').length).to.equal(1);
        expect(component.find('#TableBody').length).to.equal(1);
        expect(component.find('#TablePagination').length).to.equal(1);
        expect(component.find('#Snackbar').length).to.equal(1);
    });

});
