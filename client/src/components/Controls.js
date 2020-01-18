import React, { Component } from "react";
import Drawer from "./drawer.js";
import Navbar from "./navbar.js";
import { CSSTransition } from "react-transition-group";

class AppControls extends Component {
  state = {
    isOpen: false
  };

  toggle = () => {
    this.setState({
      isOpen: !this.state.isOpen
    });
  };

  render() {
    return (
      <div className="fixed-top">
        <Navbar toggle={this.toggle} />
        <CSSTransition in={this.state.isOpen} timeout={150} classNames="fade">
          <Drawer isOpen={this.state.isOpen} toggle={this.toggle} />
        </CSSTransition>
      </div>
    );
  }
}

export default AppControls;
