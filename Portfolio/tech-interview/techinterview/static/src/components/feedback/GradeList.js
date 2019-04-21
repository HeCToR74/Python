import React from 'react';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';
import ControlTableGrade from 'src/components/feedback/ControlTableGrade';
import {NavLink} from 'react-router-dom';

/**
 * Component that illustrates all sections and
 * allows CRUD ops with sections
 * @return {*} - Return bundled object
 */
export default function GradeList() {
//    return (
//    <h1>hello</h1>
//    )
  return (
    <div>
      <ControlTableGrade/>
      <br/>
      <NavLink to={'/grade/new'}>
        <Fab color="primary">
          <AddIcon />
        </Fab>
      </NavLink>

    </div>
  )
}
