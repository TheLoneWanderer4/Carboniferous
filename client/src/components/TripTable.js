import React from "react";
import { Table, Container } from "reactstrap";
import PropTypes from "prop-types";
import TripTableRow from "./TripTableRow";
import TripModal from "./TripModal";

import { connect } from "react-redux";

import { requestMap } from "../actions/carbonActions";

class TripTable extends React.Component {
  state = {
    modal: false,
    modalData: {}
  };

  onClick = () => {
    this.setState({ modal: !this.state.modal });
  };

  openModal = data => {
    this.onClick();
    this.setState({ modalData: data });
  };

  getTripString = steps => {
    let trip = " ";
    for (var i = 0; i < steps.length; i++) {
      trip += steps[i].current_city + " ✈️ ";
    }
    trip = trip.substring(0, trip.length - 3);
    return trip;
  };

  requestTripMap = req => {
    this.props.requestMap(req);
  };

  renderTable() {
    var i = 0;
    if (this.props.paths.length > 0) {
      return this.props.paths.map(trip => {
        i++;
        return (
          <TripTableRow
            num={i}
            key={i}
            carbon_cost={trip.total_carbon}
            total_dollars={trip.total_dollars}
            total_time={trip.total_time}
            steps={trip.steps}
            tripLabel={this.getTripString(trip.steps)}
            onClick={() => this.openModal(trip)}
          />
        );
      });
    }
  }

  render() {
    return (
      <Container>
        <Table hover responsive bordered>
          <thead>
            <tr>
              <th>Click for Details</th>
              <th>Carbon Cost</th>
              <th>Dollars Cost</th>
              <th>Time Cost</th>
              <th>Steps </th>
            </tr>
          </thead>
          <tbody>{this.renderTable()}</tbody>
        </Table>
        <TripModal
          className="modal-lg"
          label={this.getTripString(this.state.modalData.steps || "Empty")}
          data={this.state.modalData}
          modal={this.state.modal}
          toggle={this.onClick}
          requestMap={req => this.requestTripMap(req)}
          link={this.props.link}
        />
      </Container>
    );
  }
}

TripTable.propTypes = {
  paths: PropTypes.array.isRequired
};

const mapStateToProps = state => {
  return { paths: state.item.paths, link: state.item.link };
};

export default connect(
  mapStateToProps,
  { requestMap }
)(TripTable);
