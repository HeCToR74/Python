import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { CreateInterview } from '../../src/components/interview/CreateInterview';
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';


configure({ adapter: new Adapter() });

describe('interview component', () => {
    let props;

    beforeEach(() => {
        props = {
            match: {
                params: {
                    id: null,
                },
            },
            classes: {
              button: "Register-button-75",
              display: "Register-display-72",
              fontFamily: "Register-fontFamily-64",
              height: "Register-height-65",
              labelField: "Register-labelField-73",
              margin: "Register-margin-67",
              marginLeft: "Register-marginLeft-68",
              minWidth: "Register-minWidth-69",
              position: "Register-position-70",
              root: "Register-root-76",
              textAlign: "Register-textAlign-71",
              textField: "Register-textField-74",
              width: "Register-width-66",
            },
        };
    });

    const setup = () => shallow(<CreateInterview {...props} />);

    const loadState = component => component.setState( {
        depField: [{id: 1, name: "1_department"}, {id: 2, name: "2_department"},],
        canField: [{auth: {
            id: 24, 
            username: "mykola16", 
            first_name: "Андрій", 
            last_name: "Українець", 
            email: "alpaster85@gmail.com"
        }}, ],
        expField: [{auth: {
            id: 25, 
            username: "mykfola16", 
            first_name: "Андfрій", 
            last_name: "Укрfаїнець", 
            email: "alpfsfaster85@gmail.com"
        }}, ],
    });

        it('Objects is renders', () => {
            const component = setup();
            expect(component.find('#department').length).to.equal(1);
            expect(component.find('#candidate').length).to.equal(1);
            expect(component.find('#expert').length).to.equal(1);
            expect(component.find('form').length).to.equal(1);
            expect(component.find('#Button').length).to.equal(1);
        });

        it('Button is disabled', () => {
            const component = setup();
            expect(component.find('#Button').prop('disabled')).to.equal(true);
        });

        it('SelectFields are empty', () => {
            const component = setup();
            expect(component.state().values).to.deep.equal(undefined);
        });

   

    it('Button is enabled', () => {
        const component = setup();
        loadState(component);
        component.find('#department').simulate('change', { target: {value: 2 }});
        component.find('#candidate').simulate('change',  { target: {value: 24 }});
        component.find('#expert').simulate('change',  { target: {value: 25 }});

        expect(component.find('#Button').prop('disabled')).to.equal(false);
    });

    it('SelectFields are changed', () => {
        const component = setup();
        loadState(component);

        component.find('#department').simulate('change',  { target: {value: 2 }});
        component.find('#candidate').simulate('change',  { target: {value: 24 }});
        component.find('#expert').simulate('change',  { target: {value: 25 }});

        expect(component.state().DepartmentValue).to.equal(2);
        expect(component.state().CandidateValue).to.equal(24);
        expect(component.state().ExpertValue).to.equal(25);
    });
});
