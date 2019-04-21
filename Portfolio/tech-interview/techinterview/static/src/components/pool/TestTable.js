import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import {TestCell} from 'src/components/pool/TestCell';

/**
 * Render table with questions
 * @param {*} props - data from parent object
 * @return {*} - render object
 */
export function TestTable(props) {
  return (
    <div>
      <Table height={'300px'}>
        <TableHead displaySelectAll={false}
                     adjustForCheckbox={false}>
          <TableRow>
            <TableCell>Question</TableCell>
            <TableCell>Like to do</TableCell>
            <TableCell>Self-estimating</TableCell>
          </TableRow>
        </TableHead>
        <TableBody displayRowCheckbox={false}>
          {props.data.map((question) => (
            <TestCell key={question.id}
              questionID={question.id}
              name={question.name} />
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
