import React from 'react';
import {NavLink} from 'react-router-dom';
import {ControlTableQuestion} from 'src/components/question/ControlTableQuestion';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';

/**
 * Component that illustrates all questions and
 * allows CRUD ops with questions
 * @return {*} - Return bundled object
 */
export default function QuestionList() {
  return (
    <div>
      <ControlTableQuestion/>
      <br/>
      <NavLink to={'/question/new'}>
        <Fab color="primary" >
          <AddIcon />
        </Fab>
      </NavLink>
    </div>
  );
}
