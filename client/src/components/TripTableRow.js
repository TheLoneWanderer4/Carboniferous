import React from "react";

export default props => {
  return (
    <tr onClick={props.onClick}>
      <th scope="row">{props.num}</th>
      <td>{parseFloat(props.carbon_cost).toFixed(2)} kgOfCarbon</td>
      <td>${parseFloat(props.total_dollars).toFixed(2)}</td>
      <td>{parseFloat(props.total_time).toFixed(2)} Hours</td>
      <td>{props.tripLabel}</td>
    </tr>
  );
};
