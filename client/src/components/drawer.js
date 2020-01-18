import React from "react";
import { Nav, NavItem, NavLink, Container, NavbarBrand } from "reactstrap";

function Drawer(props) {
  return (
    <div>
      {props.isOpen && (
        <div className="h-100 w-100 d-flex fixed-top">
          <Container className="drawer h-100 shadow-lg text-center bg-dark">
            <NavbarBrand
              href="/"
              className="bg-secondary text-light mt-5 w-100"
            >
              Carboniferous
            </NavbarBrand>
            <Nav vertical className="mt-2">
              <NavItem>
                <NavLink href="https://github.com/TheLoneWanderer4/Carboniferous">
                  Github
                </NavLink>
              </NavItem>
            </Nav>
          </Container>
          <div id="close" className="h-100 w-100" onClick={props.toggle}></div>
        </div>
      )}
    </div>
  );
}

export default Drawer;
