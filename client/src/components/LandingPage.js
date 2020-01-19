import React from "react";
import { Jumbotron, Button, Container } from "reactstrap";
import logo from "./Free_Pine_Cones_Vector.png";

const Example = props => {
  return (
    <Container className="landing d-flex align-items-center justify-content-center">
      <Jumbotron className="shadow-lg w-100">
        <div className="d-flex flex-column flex-lg-row justify-content-around align-items-center">
          <h1 className="display-4">Carboniferous</h1>
          <img src={logo} alt="acorn" />
        </div>
        <p className="lead">
          Reducing your travel’s carbon impact for a greener future
        </p>
        <hr className="my-2" />
        <p>
          Amin Sennour • Amanda Bertsch • Mood Gladney • Joseph Acevedo ❘ HackAZ
          2020
        </p>
      </Jumbotron>
    </Container>
  );
};

export default Example;
