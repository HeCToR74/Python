import React from 'react';
import {NavLink} from 'react-router-dom';
import {ControlTableStage} from 'src/components/question/ControlTableStage';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';

/**
 * Component that illustrates all sections and
 * allows CRUD ops with sections
 * @return {*} - Return bundled object
 */
export default function StageList() {
  return (
    <div>
      <ControlTableStage/>
      <br/>
      <NavLink to={'/stage/new'}>
        <Fab color="primary" aria-label="Add" >
          <AddIcon />
        </Fab>
      </NavLink>
    </div>
  );
}
