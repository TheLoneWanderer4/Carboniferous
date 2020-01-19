import React from "react";

export default props => {
  return (
    <tr onClick={props.onClick}>
      <th scope="row">{props.num}</th>
      <td>{props.carbon_cost}</td>
      <td>{props.total_dollars}</td>
      <td>{props.total_time}</td>
      <td>{props.tripLabel}</td>
    </tr>
  );
};
