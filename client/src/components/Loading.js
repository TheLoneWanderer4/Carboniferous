import React from "react";
import { connect } from "react-redux";
import { Spinner } from "reactstrap";

function Loading(props) {
  if (props.loading) {
    return (
      <div className="loading fixed-top d-flex flex-column justify-content-center align-items-center">
        <Spinner className="spinner" color="primary" />
      </div>
    );
  } else {
    return <div></div>;
  }
}

const mapStateToProps = state => ({ loading: state.item.loading });

export default connect(mapStateToProps)(Loading);
