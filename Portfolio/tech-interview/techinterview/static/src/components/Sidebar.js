import React from 'react';
import Drawer from 'material-ui/Drawer';
import MenuItem from 'material-ui/MenuItem';
import Divider from 'material-ui/Divider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import NavLink from 'react-router-dom/es/NavLink';

/**
 * Sidebar component for home page
 * @param {props} props Some data that pushes with mounting of component
 * @return {*} Returns component
 */
export default function Sidebar(props) {
  return (
    <div>
      <Drawer width={200} open={true}>
        <div
          style={{
            marginTop: parseInt(getMuiTheme().toolbar.height + 15)+'px',
          }}
          id='Menu'
        >
        <NavLink to={'/home/'}>
          <MenuItem id='Home'>Home</MenuItem>
         </NavLink>
           <NavLink to={'/profile/'}>
          <MenuItem id='Manage Profile'>Manage Profile</MenuItem>
          </NavLink>
          <NavLink to={'/section/'}>
            <MenuItem id='section'>Sections</MenuItem>
          </NavLink>
          <NavLink to={'/stage/'}>
            <MenuItem id='stage'>Stages</MenuItem>
          </NavLink>
          <NavLink to={'/question/'}>
            <MenuItem id='question'>Questions</MenuItem>
          </NavLink>
          <NavLink to={'/department/'}>
            <MenuItem id='department'>Departments</MenuItem>
          </NavLink>
          <NavLink to={'/interview/'}>
            <MenuItem id='interview'>Interviews</MenuItem>
          </NavLink>
          <NavLink to={'/analytics/'}>
            <MenuItem id='Analytics'>Analytics</MenuItem>
          </NavLink>
          <NavLink to={'/grade/'}>
            <MenuItem id='Grades'>Grades</MenuItem>
          </NavLink>
          <Divider />
        </div>

      </Drawer>
    </div>
  );
}
