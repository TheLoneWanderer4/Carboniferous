import React from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Table
} from "reactstrap";

const ModalExample = props => {
  const { className } = props;

  const toggle = () => props.toggle();

  const links = () => {
    if (props.data.steps) {
      return props.data.steps.map(step => (
        <tr key={step.link}>
          <th scope="row">
            <a
              id="link"
              href={step.link}
              target="_blank"
              rel="noopener noreferrer"
            >
              {step.current_city}
            </a>
          </th>
          <th>{step.transport}</th>
          <th>{parseFloat(step.carbon_cost).toFixed(2)} kgOfCarbon</th>
          <th>${parseFloat(step.dollar_cost).toFixed(2)}</th>
          <th>{parseFloat(step.time_cost).toFixed(2)} Hours</th>
        </tr>
      ));
    }
  };

  return (
    <div>
      <Modal isOpen={props.modal} toggle={toggle} className={className}>
        <ModalHeader toggle={toggle}>{props.label}</ModalHeader>
        <ModalBody>
          <p>
            The total carbon footprint of this trip is{" "}
            <b className="text-primary">
              {parseFloat(props.data.total_carbon).toFixed(2)}
            </b>{" "}
            kgOfCarbon
          </p>
          <p>
            The total cost of this trip is{" "}
            <b className="text-primary">
              {parseFloat(props.data.total_dollars).toFixed(2)}
            </b>{" "}
            United States Dollars
          </p>
          <p>
            The total time of this trip is{" "}
            <b className="text-primary">
              {parseFloat(props.data.total_time).toFixed(2)}
            </b>{" "}
            Hours
          </p>

          <Table hover responsive bordered>
            <thead>
              <tr>
                <th>Stop</th>
                <th>Transport Type</th>
                <th>Carbon Cost</th>
                <th>Money Cost</th>
                <th>Time Cost</th>
              </tr>
            </thead>
            <tbody>{links()}</tbody>
          </Table>
        </ModalBody>

        <ModalFooter>
          <Button color="secondary" block onClick={toggle}>
            Close
          </Button>
        </ModalFooter>
      </Modal>
    </div>
  );
};

export default ModalExample;
