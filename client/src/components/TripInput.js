import React, { Component } from "react";
import { FormGroup, Label, Input } from "reactstrap";

function TripInput(props) {
  return (
    <div>
      <FormGroup>
        <Label for={props.name}>{props.label}</Label>
        <Input
          type={props.type}
          name={props.name}
          id={props.name}
          placeholder={props.placeholder}
          onChange={props.onChange}
        />
      </FormGroup>
    </div>
  );
}

export default TripInput;
