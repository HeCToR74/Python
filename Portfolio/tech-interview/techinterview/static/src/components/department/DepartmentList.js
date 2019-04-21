import React from 'react';
import {NavLink} from 'react-router-dom';
import {ControlTableDepartment} from 'src/components/department/ControlTableDepartment';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';

/**
 * Component that illustrates all sections and
 * allows CRUD ops with sections
 * @return {*} - Return bundled object
 */
export default function DepartmentList() {
  return (
    <div>
      <ControlTableDepartment/>
      <br/>
      <NavLink to={'/department/new/'}>
        <Fab color="primary">
          <AddIcon />
        </Fab>
      </NavLink>

    </div>
  );
}
