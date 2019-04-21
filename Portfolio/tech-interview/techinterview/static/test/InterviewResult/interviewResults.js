import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';

import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import InterviewResults from "src/components/interview/results/InterviewResults";

configure({ adapter: new Adapter() });

describe('InterviewResults component', () => {
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

 const setup = () => shallow(<InterviewResults {...props} />);
 const loadState = component => component.setState(
   { department: {sections: {Act: {Stage1:[{id:1, name:'question1'},{id:2, name:'question2'}]},
         Skills:{Stage1:[{id:3, name:'question1'},{id:4, name:'question2'}]}}
   },
     answers: {1:{answer_like: true, grade:1},
               2:{answer_like: true, grade:1},
               3:{answer_like: true, grade:1},
               4:{answer_like: true, grade:1}},
     candidate: 'FN LN',
     statuses: {1: "Middle",
                2: "Senior",
                3: "Lead",
                4: "Senior"},
     comments: {1:{validated_grade: true, comment:1},
               2:{validated_grade: true, comment:1},
               3:{validated_grade: true, comment:1},
               4:{validated_grade: true, comment:1}},
     grades: {1: "None",
              2: "Beginner",
              3: "Intermediate",
              4: "Master"},
     level: 'Senior',
   });

 context('Initial state of create form', () => {
   it('Section names is renders', () => {
     const component = setup();
     loadState(component);
     expect(component.find('h3').length).to.equal(2);
   });
   it('TableRows is renders', () => {
     const component = setup();
     loadState(component);
     expect(component.find('WithStyles(TableRow)').length).to.equal(6);
   });
   it('Tables is render', () => {
     const component = setup();
     loadState(component);
     console.log(component.debug());
     expect(component.find('WithStyles(Table)').length).to.equal(2);
   });
   it('TableCells is render', () => {
     const component = setup();
     loadState(component);
     expect(component.find('WithStyles(TableCell)').length).to.equal(36);
   });
   it('Stages is render', () => {
     const component = setup();
     loadState(component);
     expect(component.find('h2').length).to.equal(2);
   });
   it('Tabs is renders', () => {
     const component = setup();
     loadState(component);
     expect(component.find('WithStyles(Tab)').length).to.equal(2);
   });
 });

});