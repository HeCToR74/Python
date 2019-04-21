import React from 'react';
import { ControlTable } from 'src/components/question/ControlTable';
import { NavLink } from 'react-router-dom';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';

/**
 * Component that illustrates all sections and
 * allows CRUD ops with sections
 * @return {*} - Return bundled object
 */
export default function SectionList() {
  return (
    <div>
      <ControlTable />
      <br/>
      <NavLink to={'/section/new'}>
        <Fab color="primary" >
          <AddIcon />
        </Fab>
      </NavLink>
    </div>
  );
}
