import React from 'react';
import {NavLink} from 'react-router-dom';
import {ControlTableInterview} from 'src/components/interview/ControlTableInterview';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';


/**
 * Component that illustrates all sections and
 * allows CRUD ops with sections
 * @return {*} - Return bundled object
 */
export default function InterviewList() {
  return (
    <div>
      <ControlTableInterview/>
      <br/>
      <NavLink to={'/interview/new'}>
        <Fab color="primary">
          <AddIcon />
        </Fab>
      </NavLink>
    </div>
  );
}
