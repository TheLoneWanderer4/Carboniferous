import React, { Component } from "react";
import {
  Container,
  Col,
  Row,
  Button,
  Form,
  FormGroup,
  Label,
  Input,
  CustomInput
} from "reactstrap";

import TripInput from "./TripInput.js";

import { connect } from "react-redux";
import { requestCarbon } from "../actions/carbonActions";

class TripForm extends Component {
  state = {
    start: "",
    end: "",
    Date: "",
    partySize: "",
    maxPrice: "",
    maxTime: "",
    modes: {
      car: { allowed: true, mpg: 0 },
      bus: { allowed: true },
      plane: { allowed: true },
      train: { allowed: true }
    }
  };

  onSubmit = e => {
    e.preventDefault();
    this.props.requestCarbon(this.state);
  };

  onChange = e => {
    var state = this.state;

    if (Object.getOwnPropertyNames(this.state.modes).includes(e.target.name)) {
      state.modes[e.target.name].allowed = !this.state.modes[e.target.name]
        .allowed;
    } else {
      state[e.target.name] = e.target.value;
    }

    this.setState({
      ...state
    });
  };

  mpgChange = e => {
    var state = this.state;
    state.modes.car.mpg = e.target.value;
    this.setState({ ...state });
  };

  mpgInput() {
    if (this.state.modes.car.allowed) {
      return (
        <Input
          required
          className="ml-2"
          name="mpg"
          id="mpg"
          type="number"
          min="0"
          placeholder="Enter your car's MPG "
          onChange={this.mpgChange}
        />
      );
    }
  }

  render() {
    return (
      <Container className="form">
        <Form onSubmit={this.onSubmit} role="form">
          <Row form>
            <Col md={5}>
              <TripInput
                name="start"
                placeholder="Where are you starting?"
                label="Starting City"
                type="text"
                onChange={this.onChange}
              />
            </Col>
            <Col md={5}>
              <TripInput
                name="end"
                placeholder="Destination"
                label="Destination"
                type="text"
                onChange={this.onChange}
              />
            </Col>
            <Col md={2}>
              <TripInput
                name="Date"
                placeholder=""
                label="Date of Trip"
                type="date"
                onChange={this.onChange}
              />
            </Col>
          </Row>
          <Row form>
            <Col md={4}>
              <TripInput
                name="partySize"
                placeholder="People"
                label="Party Size"
                type="number"
                min="0"
                onChange={this.onChange}
              />
            </Col>
            <Col md={4}>
              <TripInput
                name="maxPrice"
                placeholder="Dollars"
                label="Max Cost"
                type="number"
                min="0"
                onChange={this.onChange}
              />
            </Col>
            <Col md={4}>
              <TripInput
                name="maxTime"
                placeholder="Hours"
                label="Max Travel Time"
                type="number"
                min="0"
                onChange={this.onChange}
              />
            </Col>
          </Row>
          <Row form>
            <FormGroup>
              <Label for="methods">Checkboxes</Label>
              <div>
                <div className="d-flex flex-row">
                  <CustomInput
                    checked={this.state.modes.car.allowed}
                    type="switch"
                    name="car"
                    id="methods"
                    label="Car"
                    onChange={this.onChange}
                  />
                  {this.mpgInput()}
                </div>

                <CustomInput
                  checked={this.state.modes.plane.allowed}
                  type="switch"
                  name="plane"
                  id="methods2"
                  label="Plane"
                  onChange={this.onChange}
                />
                <CustomInput
                  checked={this.state.modes.bus.allowed}
                  type="switch"
                  name="bus"
                  id="methods3"
                  label="Bus"
                  onChange={this.onChange}
                />

                <CustomInput
                  checked={this.state.modes.train.allowed}
                  type="switch"
                  name="train"
                  id="methods4"
                  label="Train"
                  onChange={this.onChange}
                />
              </div>
            </FormGroup>
          </Row>
          <FormGroup>
            <Button type="submit">Submit</Button>
          </FormGroup>
        </Form>
      </Container>
    );
  }
}

const mapStateToProps = state => ({});

export default connect(
  mapStateToProps,
  { requestCarbon }
)(TripForm);
