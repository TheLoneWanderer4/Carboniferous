import React from "react";
import { Navbar, NavbarToggler, NavbarBrand } from "reactstrap";

function AppNavBar(props) {
  return (
    <div className="h-100 mb-3">
      <Navbar color="dark" dark>
        <NavbarToggler
          onClick={props.toggle}
          className="mr-auto"
        ></NavbarToggler>
        <NavbarBrand href="/"> Carboniferous </NavbarBrand>
      </Navbar>
    </div>
  );
}

export default AppNavBar;
